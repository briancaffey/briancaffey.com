from django.shortcuts import render
from .models import Project
from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.resources import CDN

from django.shortcuts import render, render_to_response

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

# Create your views here.
def projects_home(request):
	projects = Project.objects.all().order_by('order')
	context = {'projects':projects}
	return render(request, 'projects/projects_home.html', context)


# def kings(request):
# 	return render(request, 'projects/kings.html', {})
#
# def kings_two(request):
# 	return render(request, 'projects/kings_v2.html', {})
#
#
# def kings_three(request):
# 	return render(request, 'projects/kings_v3.html', {})
#
#
#
# def level_builder(request):
# 	return render(request, 'projects/level_builder.html', {})
