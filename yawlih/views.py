from django.shortcuts import render

# Create your views here.
def yl_home(request):
    return render(request, 'yawlih/yl_home.html', {})

def reports(request):
    return render(request, 'yawlih/reports.html', {})
