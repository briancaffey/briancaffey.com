from django.shortcuts import render, redirect
from .forms import NewsletterEmailsForm
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)


EMAIL_HOST_USER = settings.EMAIL_HOST_USER
# Create your views here.
def home(request):


	form_ = NewsletterEmailsForm(request.POST or None)
	login_form = UserLoginForm(request.POST or None)
	registration_form = UserRegistrationForm(request.POST or None)
	context = {
		'form_':form_,
		'login_form':login_form,
		'registration_form':registration_form,
	}


	if login_form.is_valid():
		username = login_form.cleaned_data.get('username')
		password = login_form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		messages.success(request, 'Welcome back, ' + str(request.user) + '!')
		return redirect('posts:list')


	if registration_form.is_valid():
		user = registration_form.save(commit=False)
		password = registration_form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		messages.success(request, 'Thanks for registering, ' + str(request.user.username) + '!')
		return redirect('posts:list')




	if form_.is_valid():
		instance = form_.save(commit=False)
		email = form_.cleaned_data.get('email')

		instance.save()
		send_mail('Thanks for signing up for my Newsletter!', 'Hi, thanks.', EMAIL_HOST_USER, [email])
		messages.success(request, "Thanks for joining the newsletter. Please check your email to confirm.")
		return redirect('home:home')

	return render(request, 'home/home.html', context)
