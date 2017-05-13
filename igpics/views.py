from django.shortcuts import render

# Create your views here.
def igpics(request):
    return render(request, 'igpics/igpics.html', {})
