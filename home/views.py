from django.shortcuts import render, redirect
from .forms import NewsletterEmailsForm
import brianblog.settings.local as settings
from django.contrib import messages
from django.core.mail import send_mail

EMAIL_HOST_USER = settings.EMAIL_HOST_USER
# Create your views here.
def home(request):


	form = NewsletterEmailsForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		email = form.cleaned_data.get('email')

		instance.save()
		send_mail('Thanks for signing up for my Newsletter!', 'Hi, thanks.', EMAIL_HOST_USER, [email])
		messages.success(request, "Thanks for joining the newsletter. Please check your email to confirm.")
		return redirect('home:home')

	context = {
		'form':form
	}

	return render(request, 'home/home.html', context)
