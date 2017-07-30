from django.shortcuts import render

# Create your views here.

def playquest_home(request):
	return render(request, 'playquest/playquest_home.html', {})

def demo(request):
	return render(request, 'playquest/demo.html', {})

def game_id(request, id):
	game = Game.objects.get(id=id)
	if game.exists():
		context = {
			'game':game,
			'game_id': id,
			}
	else:
		context = {}
	return render(request, 'playquest/game.html', context)

def create(request):
	return render(request, 'playquest/create.html', {})

def edit_game(request, id):
	return render(request, 'playquest/edit.html', {})

def sample_json(request):
	return render(request, 'playquest/sample.json', {})