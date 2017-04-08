from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.contrib.auth import (
	authenticate, 
	get_user_model, 
	login, 
	logout, 
	)

from .forms import UserLoginForm, UserRegistrationForm



# Create your views here.
def login_view(request):
	form = UserLoginForm(request.POST or None)
	print('hmm')
	print(form.errors)

	print(request.user.is_authenticated())
	if form.is_valid():
		print("text")
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		print(request.user.is_authenticated())
		messages.success(request, 'Welcome back, ' + str(request.user) + '!')
		return redirect('posts:list')

	return render(request, 'accounts/form.html', {'form':form})


def register_view(request):
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		messages.success(request, 'Thanks for registering, ' + str(request.user.username) + '!')
		return redirect('posts:list')
	context = {
		'form':form,
	}
	return render(request, 'accounts/registration_form.html', context)


def logout_view(request):
	logout(request)
	return render(request, 'accounts/logout_success.html', {})