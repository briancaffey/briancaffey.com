from django.shortcuts import render, redirect
from .forms import NewsletterEmailsForm
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from accounts.forms import UserLoginForm, UserRegistrationForm
from .forms import GuestBookForm
from .models import GuestBook
from .utils import get_client_ip
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

import requests


EMAIL_HOST_USER = settings.EMAIL_HOST_USER
# Create your views here.
def home(request):
	ip = get_client_ip(request)
	base = "http://api.ipinfodb.com/v3/ip-city/?key=3a3bdb7e563895cd7d7b27ff9c5efd60d8686be6d75ab117fe40497d3054d8e9&ip="
	query = base + ip
	r = requests.get(query)
	location = r.text.split(';')[-5]

	form_ = NewsletterEmailsForm(request.POST or None)
	login_form = UserLoginForm(request.POST or None)
	registration_form = UserRegistrationForm(request.POST or None)
	guest_form = GuestBookForm(request.POST or None)
	guest_book = GuestBook.objects.all()

	# ip_lookup = pyipinfodb.IPInfo('3a3bdb7e563895cd7d7b27ff9c5efd60d8686be6d75ab117fe40497d3054d8e9')
	# ip_lookup.get_city(get_client_ip(request))
	# city = get_client_ip(request)

	context = {
		'form_':form_,
		'login_form':login_form,
		'registration_form':registration_form,
		'guest_form':guest_form,
		'guest_book':guest_book,
		'ip':ip,
		'city':location,
	}

	if request.method == "POST":
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
			form_ = NewsletterEmailsForm(None)
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

		if guest_form.is_valid():
			instance = guest_form.save(commit=False)
			if location:
				instance.city = location
			if request.user.is_authenticated():
				instance.user = request.user
			instance.save()
			messages.success(request, "Thank you for signing the guest book!")
			return redirect('home:home')

	return render(request, 'home/home.html', context)
