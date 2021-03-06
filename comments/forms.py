from django import forms

class CommentForm(forms.Form):
	content_type = forms.CharField(widget=forms.HiddenInput)
	object_id = forms.IntegerField(widget=forms.HiddenInput)
	#parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
	content = forms.CharField(label='', widget=forms.Textarea(
		attrs={'rows':3, 'id':'post-text'}))

class GuestBookForm(forms.Form):
	message = forms.CharField()
	object_id = forms.IntegerField(widget=forms.HiddenInput)
	#parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
	content = forms.CharField(label='', widget=forms.Textarea(
		attrs={'rows':3}))
