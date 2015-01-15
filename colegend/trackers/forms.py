from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from lib.crispy import SaveButton, CancelButton
from tags.models import Tag
from trackers.models import Weight, Sex, Book, Joke, Transaction

__author__ = 'eraldo'


class WeightForm(ModelForm):
    class Meta:
        model = Weight
        fields = ['time', 'weight', 'notes']

    helper = FormHelper()
    helper.layout = Layout(
        Field('time'),
        Field('weight', autofocus='True'),
        Field('notes', rows=2),
        SaveButton(),
        CancelButton(),
    )


class SexForm(ModelForm):
    class Meta:
        model = Sex
        fields = ['date', 'amount', 'person', 'notes']

    helper = FormHelper()
    helper.layout = Layout(
        Field('date'),
        Field('amount', autofocus='True'),
        Field('person'),
        Field('notes', rows=2),
        SaveButton(),
        CancelButton(),
    )


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'status', 'url', 'notes']

    helper = FormHelper()
    helper.layout = Layout(
        Field('title', autofocus='True'),
        Field('author'),
        Field('status'),
        Field('url'),
        Field('notes', rows=2),
        SaveButton(),
        CancelButton(),
    )


class JokeForm(ModelForm):
    class Meta:
        model = Joke
        fields = ['name', 'description', 'notes', 'rating']

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True'),
        Field('description'),
        Field('notes', rows=2),
        Field('rating'),
        SaveButton(),
        CancelButton(),
    )


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['time', 'amount', 'transaction_type', 'description', 'category', 'tags', 'notes']

    helper = FormHelper()
    helper.layout = Layout(
        Field('time'),
        Field('amount', autofocus='True'),
        Field('transaction_type'),
        Field('description'),
        Field('category'),
        Field('tags'),
        Field('notes', rows=2),
        SaveButton(),
        CancelButton(),
    )
