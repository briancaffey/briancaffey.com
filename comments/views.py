from django.shortcuts import render, get_object_or_404

from .models import Comment

# Create your views here.
def comment_thread(request, pk):
	obj = get_object_or_404(Comment, pk=pk)
	context = {
		'comment':obj,
	}
	return render(request, 'comments/comment_thread.html', context)