from .form import LandingApplyForm
from django.shortcuts import render
from .models import LandingApply
from .models import Item
from django.views.generic import ListView, DetailView, CreateView


class ItemListView(ListView):
    model = Item

    def get_queryset(self):
        return Item.objects.order_by('-item_created')


class LandingApplyDetail(DetailView):
    model = LandingApply

    def get_queryset(self):
        return LandingApply.objects.order_by('-apply_created')


class LandingApplyCreateView(CreateView):
    model = LandingApply
    form_class = LandingApplyForm

    # def form_valid(self, form):
    #     current_user = self.request.user
    #     if current_user.is_authenticated:
    #         form.instance.author = current_user
    #         return super(type(self), self).form_valid(form)
    #     else:
    #         return redirect('/onedeal')

