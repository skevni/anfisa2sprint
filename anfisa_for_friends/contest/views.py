from django.shortcuts import render

from contest.forms import ContestForm


def proposal(request):
    form = ContestForm(request.POST or None)
    context = {'form': form}
    return render(request, 'contest/form.html', context=context)
