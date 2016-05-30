from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from django.core.urlresolvers import reverse

from colegend.core.forms import OwnedModelForm
from colegend.tags.fields import TagsCreateFormField
from .models import Outcome

from django.utils.translation import ugettext_lazy as _

class OutcomeFilterForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = [
            'name',
            'description',
            'status',
            'inbox',
            'review',
            'date',
            'deadline',
            'estimate',
            'tags',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Update the tags field to use the custom django-autocomplete's create field
        tags_queryset = self.fields.get('tags').queryset
        self.fields['tags'] = TagsCreateFormField(tags_queryset, required=False)

        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.form_class = 'filter-form'

        self.helper.layout = Layout(
            Field('name'),
            Field('description'),
            Field('status'),
            Field('inbox'),
            Field('review'),
            Field('date'),
            Field('deadline'),
            Field('estimate'),
            Field('tags'),
        )
        self.helper.add_input(Submit('filter', 'Filter'))


class OutcomeForm(OwnedModelForm):
    class Meta:
        model = Outcome
        fields = [
            'owner',
            'name',
            'description',
            'status',
            'inbox',
            'review',
            'date',
            'deadline',
            'estimate',
            'tags',
        ]

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner', None)
        super().__init__(*args, **kwargs)
        # Update the tags field to use the custom django-autocomplete's create field
        tags_queryset = self.fields.get('tags').queryset
        self.fields['tags'] = TagsCreateFormField(tags_queryset, required=False)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('owner', type="hidden"),
            Field('name'),
            Field('description'),
            Field('status'),
            Field('inbox'),
            Field('review'),
            Field('date'),
            Field('deadline'),
            Field('estimate'),
            Field('tags'),
        )
        self.helper.add_input(Submit('save', 'Save'))


class OutcomeQuickCreateForm(OwnedModelForm):
    class Meta:
        model = Outcome
        fields = [
            'owner',
            'name',
            'status',
        ]

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner', None)
        next_url = kwargs.pop('next', None)
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False

        action_url = reverse('outcomes:create')
        if next_url:
            action_url += '?next={}'.format(next_url)
        self.helper.form_action = action_url

        self.helper.layout = Layout(
            Field('owner', type="hidden"),
            Field('name', placeholder=_('New outcome..'), autofocus=True),
            Field('status', type="hidden"),
        )