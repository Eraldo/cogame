from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from habits.models import Habit
from lib.views import OwnedItemsMixin

__author__ = 'eraldo'


class HabitMixin(LoginRequiredMixin, OwnedItemsMixin):
    model = Habit
    fields = ['routine', 'name', 'tags']

    def get_form(self, form_class):
        form = super(HabitMixin, self).get_form(form_class)
        # limit routine choices to owned routines
        routines = form.fields['routine'].queryset
        form.fields['routine'].queryset = routines.owned_by(self.request.user)
        return form


class HabitListView(HabitMixin, ListView):
    pass


class HabitNewView(HabitMixin, CreateView):
    success_url = reverse_lazy('habits:habit_list')

    def get_initial(self):
        initial = super(HabitNewView, self).get_initial()
        routine = self.request.GET.get('routine')
        if routine:
            initial['routine'] = routine
        return initial

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super(HabitNewView, self).form_valid(form)


class HabitShowView(HabitMixin, DetailView):
    template_name = "habits/habit_show.html"


class HabitEditView(HabitMixin, UpdateView):
    success_url = reverse_lazy('habits:habit_list')


class HabitDeleteView(HabitMixin, DeleteView):
    success_url = reverse_lazy('habits:habit_list')