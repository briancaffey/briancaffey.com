from django.shortcuts import render

# Create your views here.
def hashitemtest(request):
    return render(request, 'hashtest/hashtest.html', {})
