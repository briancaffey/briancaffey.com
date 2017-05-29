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


def kings(request):
	return render(request, 'projects/kings.html', {})
# def bokeh(request):
# 	plot = figure()
# 	plot.circle([1,2], [3,4])
#
# 	script, div = components(plot, CDN)
#
# 	return render(request, "projects/bokeh.html", {"the_script":script, "the_div":div})
#



def bokeh(request):
	x= [1,3,5,7,9,11,13]
	y= [1,2,3,4,5,6,7]
	title = 'y = f(x)'

	plot = figure(title= title ,
		x_axis_label= 'X-Axis',
		y_axis_label= 'Y-Axis',
		plot_width =400,
		plot_height =400)

	plot.line(x, y, legend= 'f(x)', line_width = 2)
	#Store components
	script, div = components(plot)

	#Feed them to the Django template.
	return render_to_response( 'projects/bokeh.html', {'script' : script , 'div' : div} )
