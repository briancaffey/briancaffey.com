from django.shortcuts import render
from .models import Game


def kings_home(request):
	return render(request, 'kings/kings_home.html', {})

def demo(request):
	return render(request, 'kings/demo.html', {})

def game_id(request, id):
	game = Game.objects.filter(id=id)
	if len(game) == 1:
		context = {
			'game':game,
			'game_id': id,
			}
	else:
		context = {}
	return render(request, 'kings/game.html', context)

def create(request):
	return render(request, 'kings/create.html', {})

def sample_json(request):
	return render(request, 'kings/sample.json', {})
