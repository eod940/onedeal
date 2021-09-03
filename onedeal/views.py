from django.shortcuts import render
from .models import LandingApply
from .models import Item
from django.views.generic import ListView


class LandingApplyList(ListView):
    model = Item

    def get_queryset(self):
        return Item.objects.order_by('-item_created')

