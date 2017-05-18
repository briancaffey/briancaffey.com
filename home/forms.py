from django import forms



from .models import NewsletterEmails, GuestBook

class NewsletterEmailsForm(forms.ModelForm):

	# email = forms.EmailField()

	class Meta:
		model = NewsletterEmails
		fields = ['email',]

		widgets = {
			'email': forms.TextInput(
				attrs={'id':'email', 'required':True, 'placeholder':'enter your email'}
			)
		}

	def __init__(self, *args, **kwargs):
	    super(NewsletterEmailsForm, self).__init__(*args, **kwargs)
	    self.fields['email'].label = ''

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = NewsletterEmails.objects.filter(email=email)
		if qs.count() == 1:
			raise forms.ValidationError("you have already joined the newsletter")

		return email


class GuestBookForm(forms.ModelForm):

	class Meta:
		model = GuestBook
		fields = [
			'message',
		]
		widgets = {
			'message': forms.TextInput(
				attrs={'id':'post-text', 'label':'something', 'required':True, 'placeholder':'leave me a message here.'}
			)
		}

	def __init__(self, *args, **kwargs):
	    super(GuestBookForm, self).__init__(*args, **kwargs)
	    self.fields['message'].label = ''

	def clean_message(self):
		message = self.cleaned_data.get('message')
		if message.strip(' ') == "":
			raise forms.ValidationError("please add a note before submitting. thanks!")
		return message
