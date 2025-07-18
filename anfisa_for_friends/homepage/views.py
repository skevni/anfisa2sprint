from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    context = {
        "ice_creams":
        IceCream.objects.values("id", "title", "description")
        .filter(
            Q(is_published=True) & Q(is_on_main=True)
        ).order_by('title')[1:4]
    }

    return render(request, template, context)
