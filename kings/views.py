from django.shortcuts import render

# Create your views here.
def kings(request):
	return render(request, 'kings/kings.html', {})

def kings_two(request):
	return render(request, 'kings/kings_v2.html', {})


def kings_three(request):
	return render(request, 'kings/kings_v3.html', {})



def level_builder(request):
	return render(request, 'kings/level_builder.html', {})
