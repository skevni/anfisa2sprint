from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    context = {
        "ice_cream_list":
        IceCream.objects.values("id", "title", "description")
        .filter(
            Q(is_published=True) & Q(is_on_main=True) &
            Q(category__is_published=True)
        ).order_by('output_order', 'title')[1:4]
    }

    return render(request, template, context)
