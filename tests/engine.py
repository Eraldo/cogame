from subprocess import call
from os import path, getcwd
import hitchpostgres
import hitchselenium
import hitchpython
import hitchserve
import hitchredis
import hitchtest
import hitchsmtp
from time import sleep

# Get directory above this file
PROJECT_DIRECTORY = path.abspath(path.join(path.dirname(__file__), '..'))

# Get the static files path for the tests (used for upload)
STATIC_TEST_FILES_PATH = path.join(getcwd(), 'static', 'tests')


class ExecutionEngine(hitchtest.ExecutionEngine):
    """Engine for orchestating and interacting with the app."""

    def set_up(self):
        """Ensure virtualenv present, then run all services."""
        python_package = hitchpython.PythonPackage(
            python_version=self.settings['python_version']
        )
        python_package.build()

        call([
            python_package.pip, "install", "-r",
            path.join(PROJECT_DIRECTORY, "requirements/local.txt")
        ])

        postgres_package = hitchpostgres.PostgresPackage()
        postgres_package.build()

        redis_package = hitchredis.RedisPackage()
        redis_package.build()

        self.services = hitchserve.ServiceBundle(
            project_directory=PROJECT_DIRECTORY,
            startup_timeout=float(self.settings["startup_timeout"]),
            shutdown_timeout=float(self.settings["shutdown_timeout"]),
        )

        # Docs : https://hitchtest.readthedocs.org/en/latest/plugins/hitchpostgres.html

        # Postgres user and database
        postgres_user = hitchpostgres.PostgresUser("colegend", "password")

        self.services['Postgres'] = hitchpostgres.PostgresService(
            postgres_package=postgres_package,
            users=[postgres_user, ],
            databases=[hitchpostgres.PostgresDatabase("colegend", postgres_user), ]
        )

        # Docs : https://hitchtest.readthedocs.org/en/latest/plugins/hitchsmtp.html
        self.services['HitchSMTP'] = hitchsmtp.HitchSMTPService(port=1025)

        # Docs : https://hitchtest.readthedocs.org/en/latest/plugins/hitchredis.html
        self.services['Redis'] = hitchredis.RedisService(
            redis_package=redis_package,
            port=16379,
        )

        # Docs : https://hitchtest.readthedocs.org/en/latest/plugins/hitchpython.html
        self.services['Django'] = hitchpython.DjangoService(
            python=python_package.python,
            port=8800,
            settings="config.settings.test",
            needs=[self.services['Postgres'], ],
            env_vars=self.settings['environment_variables'],
        )

        # self.services['Celery'] = hitchpython.CeleryService(
        #     python=python_package.python,
        #     app="{{cookiecutter.repo_name}}.taskapp", loglevel="INFO",
        #     needs=[
        #         self.services['Redis'], self.services['Django'],
        #     ],
        #     env_vars=self.settings['environment_variables'],
        # )

        # Docs : https://hitchtest.readthedocs.org/en/latest/plugins/hitchselenium.html
        self.services['Firefox'] = hitchselenium.SeleniumService(
            xvfb=self.settings.get("xvfb", False),
            no_libfaketime=True,
        )

        #        import hitchcron
        #        self.services['Cron'] = hitchcron.CronService(
        #            run=self.services['Django'].manage("trigger").command,
        #            every=1,
        #            needs=[ self.services['Django'], ],
        #        )

        self.services.startup(interactive=False)

        # Docs : https://hitchtest.readthedocs.org/en/latest/plugins/hitchselenium.html
        self.driver = self.services['Firefox'].driver

        self.webapp = hitchselenium.SeleniumStepLibrary(
            selenium_webdriver=self.driver,
            wait_for_timeout=5,
        )

        self.click = self.webapp.click
        self.wait_to_appear = self.webapp.wait_to_appear
        self.wait_to_contain = self.webapp.wait_to_contain
        self.wait_for_any_to_contain = self.webapp.wait_for_any_to_contain
        self.click_and_dont_wait_for_page_load = self.webapp.click_and_dont_wait_for_page_load

        # Configure selenium driver
        self.driver.set_window_size(self.settings['window_size']['height'], self.settings['window_size']['width'])
        self.driver.set_window_position(0, 0)
        self.driver.implicitly_wait(2.0)
        self.driver.accept_next_alert = True

    # BASIC METHODS

    def pause(self, message=None):
        """Pause test and launch IPython"""
        if hasattr(self, 'services'):
            self.services.start_interactive_mode()
        self.ipython(message)
        if hasattr(self, 'services'):
            self.services.stop_interactive_mode()

    def load_website(self):
        """Navigate to website in Firefox."""
        self.driver.get(self.services['Django'].url())

    def fill_form(self, **kwargs):
        """Fill in a form with id=value."""

        for element, text in kwargs.items():
            if isinstance(text, dict):
                text = path.join(STATIC_TEST_FILES_PATH, text.get('file'))
            try:
                self.driver.find_element_by_id(element).send_keys(text)
            except:  # Added to find case sensitive ids like "Email".
                self.driver.find_element_by_id(element.title()).send_keys(text)

    def confirm_emails_sent(self, number):
        """Count number of emails sent by app."""
        emails = len(self.services['HitchSMTP'].logs.json())
        expected_emails = int(number)
        assert emails == expected_emails, "expected {} emails - got {}".format(expected_emails, emails)

    def click_on_link_in_last_email(self, which=1):
        """Click on the nth link in the last email sent."""
        self.driver.get(
            self.services['HitchSMTP'].logs.json()[-1]['links'][which - 1]
        )

    def wait_for_email(self, containing=None):
        """Wait for, and return email."""
        self.services['HitchSMTP'].logs.out.tail.until_json(
            lambda email: containing in email['payload'] or containing in email['subject'],
            timeout=25,
            lines_back=1,
        )

    def time_travel(self, days=""):
        """Make all services think that time has skipped forward."""
        self.services.time_travel(days=int(days))

    def on_failure(self):
        """Runs if there is a test failure. Stop and IPython."""
        if not self.settings['quiet']:
            if self.settings.get("pause_on_failure", False):
                self.pause(message=self.stacktrace.to_template())

    def on_success(self):
        """Pause on success if enabled."""
        if self.settings.get("pause_on_success", False):
            self.pause(message="SUCCESS")

    def tear_down(self):
        """Shut down services required to run your test."""
        if hasattr(self, 'services'):
            self.services.shutdown()

    # EXTRA METHODS

    def connect_to_kernel(self, service_name):
        """Connect to IPython kernel embedded in service_name."""
        self.services.connect_to_ipykernel(service_name)

    def load_page(self, page):
        """Navigate to website page in Firefox."""
        self.driver.get(self.services['Django'].url() + page)

    def click_submit(self):
        """Click on a submit button if it exists."""
        self.driver.find_element_by_css_selector("button[type=\"submit\"]").click()

    def page_title(self, title):
        """Check if the browser page title matches the given title."""
        current_title = self.driver.title
        assert title in current_title, "expected title '{}' - title was '{}'".format(title, current_title)

    def find_element(self, name):
        """Find the element id or class within the dom."""
        try:
            element = self.driver.find_element_by_id(name)
        except:
            element = self.driver.find_element_by_css_selector('.{}'.format(name))
        assert element, "text '{}' was not found".format(text)

    def find_text(self, text):
        """Find the text within the dom."""
        assert self.driver.find_element_by_xpath(
            "//*[contains(.,'{}')]".format(text)), "text '{}' was not found".format(text)

    def scroll_to(self, id):
        """Scroll to an element."""
        self.driver.execute_script('$("#{}").get(0).scrollIntoView(false);'.format(id))

    def click_email_link(self, containing=None, link_text=None):
        """
        Click on a link in an email.
        :param containing: Text to search for to find the correct email.
        :param link_text: A text to be found in that link. [optional]
        :return:
        """
        email = self.services['HitchSMTP'].logs.out.tail.until_json(
            lambda email: containing in email['payload'] or containing in email['subject'],
            timeout=25,
            lines_back=1,
        )
        links = email['links']
        if link_text:
            for link in links:
                if link_text in link:
                    url = link
                    break
        else:
            url = links[0]
        self.driver.get(url)

    def execute(self, script):
        """
        Execute the javascript on the current page.
        :param script:
        :return:
        """
        self.driver.execute_script(script)

    def wait(self, seconds=1):
        """
        Wait for a given amout of seconds.
        :param seconds: The amount of seconds to wait. [default=1]
        :return:
        """
        sleep(seconds)
