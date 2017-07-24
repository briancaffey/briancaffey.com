from django.shortcuts import render
from .models import Game


# Create your views here.
def kings(request):
	return render(request, 'kings/kings.html', {})

def kings_two(request):
	return render(request, 'kings/kings_v2.html', {})


def kings_three(request):
	return render(request, 'kings/kings_v3.html', {})


def game_id(request, id):
	game = Game.objects.get(id=id)
	context = {
		'game':game,
		'game_id': id,
		}
	return render(request, 'kings/kings_v4.html', context)

def kings_four(request):

	return render(request, 'kings/kings_v4.html', {})

def sample_json(request):
	return render(request, 'kings/sample.json', {})

def level_builder(request):
	return render(request, 'kings/level_builder.html', {})
