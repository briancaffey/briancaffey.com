from django import forms

from .models import ReadingMaterial

class ReadingMaterialForm(forms.ModelForm):

	name = forms.CharField()

	description = forms.CharField(widget=forms.Textarea(
		attrs={'rows':4}))

	tags = forms.CharField(widget=forms.TextInput(
		attrs={'placeholder':'python django webdev'}))

	class Meta:
		model = ReadingMaterial
		fields = [
                'name',
                'description',
                'link',
				'tags',
			]
