from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post
import datetime

YEAR_CHOICES = tuple([2000+i for i in range(22)])

class PostForm(forms.ModelForm):

	content = forms.CharField(widget=PagedownWidget(show_preview=False))

	publish = forms.DateField(widget=forms.SelectDateWidget)

	publish = forms.DateField(
		initial = datetime.date.today,
		widget=forms.SelectDateWidget(

		years=YEAR_CHOICES)
	)

	class Meta:
		model = Post
		fields = [
			'title',
			'content',
			'image',
			'draft',
			'publish',
			]
