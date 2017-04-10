from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CommentForm
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages

# Create your views here.


@login_required
def comment_delete(request, pk):
	obj = get_object_or_404(Comment, pk=pk)
	if request.method == "POST":
		if request.user == obj.user:
			parent_object_url = obj.content_object.get_absolute_url()
			obj.delete()
			messages.success(request, "Your comment was deleted.")
			return HttpResponseRedirect(parent_object_url)
		else:
			parent_object_url = obj.content_object.get_absolute_url()
			messages.success(request, "You don't have permission to delete this comment.")
			return HttpResponseRedirect(parent_object_url)
			
	context = {
		'object':obj, 
	}



	return render(request, "confirm_delete.html", context)



def comment_thread(request, pk):
	obj = get_object_or_404(Comment, pk=pk)
	content_object = obj.content_object
	content_id = obj.content_object.id
	


	initial_data = {
		'content_type':obj.content_type, 
		'object_id':obj.object_id,
	}
	form = CommentForm(request.POST or None, initial=initial_data)
	print(form.errors)
	print(dir(form))
	if form.is_valid():
		c_type = form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = form.cleaned_data.get('object_id')
		content_data = form.cleaned_data.get('content')
		parent_obj = None
		try: 
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id: 
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists():
				parent_obj = parent_qs.first()

		new_comment, created = Comment.objects.get_or_create(
									user=request.user, 
									content_type=content_type, 
									object_id=obj_id,
									content=content_data,
									parent=parent_obj
									
							)
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())




	context = {
		'comment':obj,
		'form': form,
	}
	return render(request, 'comments/comment_thread.html', context)