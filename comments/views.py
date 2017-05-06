from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CommentForm
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from .serializers import CommentSerializer
from django.contrib.contenttypes.fields import GenericForeignKey

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, serializers

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



	return render(request, "comments/confirm_delete.html", context)



def comment_thread(request, pk):
	obj = get_object_or_404(Comment, pk=pk)
	content_object = obj.content_object
	content_id = obj.content_object.id



	initial_data = {
		'content_type':obj.content_type,
		'object_id':obj.object_id,
	}
	form = CommentForm(request.POST or None, initial=initial_data)
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

#
#
class CommentCreateAPIView(CreateAPIView):
	queryset = Comment.objects.all()
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = ()#(permissions.IsAuthenticated,)
	serializer_class = CommentSerializer
# 	serializer_class = GuestBookSerializer
#
	def perform_create(self, serializer):
		content = self.request.POST['content']
		object_id = self.request.POST['object_id']
		c_type = self.request.POST["content_type"]
		print(c_type)
		content_type = ContentType.objects.get(model=c_type)

		content_object = GenericForeignKey(content_type, object_id)
		if content.strip(' ') == "":
			raise serializers.ValidationError("Unable to accept empty guest book notes")
		if self.request.user.is_authenticated():

			_ = serializer.save(user=self.request.user, content=content, object_id=object_id, content_type=content_type, content_object=content_object)
# 		else:
# 			_ = serializer.save(message=message, city=city, state=state)

		return Response(_)
#
