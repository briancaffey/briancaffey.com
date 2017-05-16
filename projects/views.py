from django.shortcuts import render
from .models import Project

# Create your views here.
def projects_home(request):
	projects = Project.objects.all().order_by('order')
	context = {'projects':projects}
	return render(request, 'projects/projects_home.html', context)
