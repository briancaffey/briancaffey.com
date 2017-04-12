from django import forms

from .models import ReadingMaterial

class ReadingMaterialForm(forms.ModelForm):

	name = forms.CharField()

	description = forms.CharField(widget=forms.Textarea(
		attrs={'rows':4}))


	class Meta:
		model = ReadingMaterial
		fields = [
                'name',
                'description',
                'link',
				'tags',
			]
