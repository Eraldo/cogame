from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from projects.models import Project

__author__ = 'eraldo'


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'status', 'priority', 'deadline', 'tags']
        widgets = {
            'description': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True'),
        Field('description'),
        Field('status'),
        Field('priority'),
        Field('deadline'),
    )
    helper.add_input(Submit('save', 'Save'))
