from django import forms



from .models import NewsletterEmails, GuestBook

class NewsletterEmailsForm(forms.ModelForm):

	email = forms.EmailField()

	class Meta:
		model = NewsletterEmails
		fields = ['email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = NewsletterEmails.objects.filter(email=email)
		if qs.count() == 1:
			raise forms.ValidationError("You have already joined the newsletter")

		return email


class GuestBookForm(forms.ModelForm):

	class Meta:
		model = GuestBook
		fields = [
			'message',
		]
		widgets = {
			'message': forms.TextInput(
				attrs={'id':'post-text', 'required':True, 'placeholder':'Leave me a message here.'}
			)
		}
