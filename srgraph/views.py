from django.shortcuts import render, redirect

from .utils import graph_
# Create your views here.
def graph_view(request):
    context = {}
    results = graph_()
    context['results'] = results
    return render(request, 'srgraph/srgraph.html', context)
