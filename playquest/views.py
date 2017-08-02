from django.shortcuts import render
from .models import Game
from django.contrib.auth.decorators import login_required
# Create your views here.

def playquest_home(request):
	return render(request, 'playquest/playquest_home.html', {})

def demo(request):
	return render(request, 'playquest/demo.html', {})

def game_id(request, id):
	game = Game.objects.filter(id=id)
	if len(game) == 1:
		context = {
			'game':game,
			'game_id': id,
			}
	else:
		context = {}
	return render(request, 'playquest/game.html', context)

def create(request):
	return render(request, 'playquest/create.html', {})

@login_required
def edit_game(request, id):
    game = Game.objects.filter(id=id)
    context = {}
    if len(game) == 1:
        if game.first().id == request.user.id:
            print("game belongs to user")
            context = {
                'game':game.first(),
            }
        else:
            print("You can't edit this game, but you can branch it")
    else:
        context = {}
    return render(request, 'playquest/edit.html', context)

def sample_json(request):
	return render(request, 'playquest/sample.json', {})
