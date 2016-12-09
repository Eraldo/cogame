from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db import models
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailcore.models import Page

from colegend.core.fields import MarkdownField
from colegend.core.models import AutoOwnedBase, AutoUrlsMixin, OwnedQuerySet


class JournalQuerySet(OwnedQuerySet):
    pass


class Journal(AutoUrlsMixin, AutoOwnedBase):
    """
    A django model representing a user's journal.
    """

    spellchecker = models.BooleanField(default=False)
    day_template = MarkdownField(default=render_to_string('dayentries/template.md'))
    week_template = MarkdownField(default=render_to_string('weekentries/template.md'))
    month_template = MarkdownField(default=render_to_string('monthentries/template.md'))

    objects = JournalQuerySet.as_manager()

    class Meta:
        verbose_name = _('Journal')
        verbose_name_plural = _('Journals')

    def __str__(self):
        return "{}'s journal".format(self.owner)

    def reset(self):
        self.spellchecker = False
        self.day_template = render_to_string('dayentries/template.md')
        self.week_template = render_to_string('weekentries/template.md')
        self.month_template = render_to_string('monthentries/template.md')
        self.save()
        return True


class JournalPage(RoutablePageMixin, Page):
    template = 'journals/index.html'

    @route(r'^$')
    @route(r'^(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/$')
    def day(self, request, date=None):
        date = date or timezone.now().date()
        return TemplateResponse(
            request,
            self.get_template(request),
            self.get_context(request)
        )
