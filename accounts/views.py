from django.shortcuts import render


from django.contrib.auth import (
	authenticate, 
	get_user_model, 
	login, 
	logout, 
	)

from .forms import UserLoginForm



# Create your views here.
def login_view(request):
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')


	return render(request, 'form.html', {'form':form})


def register_view(request):
	return render(request, 'form.html', {})


def logout_view(request):
	return render(request, 'form.html', {})