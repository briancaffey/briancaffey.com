from urllib.parse import quote_plus
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from comments.models import Comment
from comments.forms import CommentForm
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required



from .forms import PostForm



def posts_create(request):
	# if not request.user.is_staff or not request.user.is_superuser:
	if not request.user.is_authenticated:
		raise Http404

	form = PostForm(request.POST or None, request.FILES or None)

	if form.is_valid():

		instance = form.save(commit=False)
		instance.user = request.user
		print(form.cleaned_data.get('title'))
		instance.save()
		#message success
		messages.success(request, 'Successfully Created!')
		return HttpResponseRedirect(instance.get_absolute_url())
	elif request.method=="POST":
		messages.error(request, "not Successfully created")

	context = {
		'form': form
	}
	return render(request, "post_form.html", context)


def posts_list(request):


	today = timezone.now().date()

	queryset_list = Post.objects.active()
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()
	#queryset_list = Post.objects.all().order_by("-timestamp")
	query = request.GET.get('q')
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query) |
			Q(user__first_name__icontains=query) |
			Q(user__last_name__icontains=query)
			).distinct()

	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		'object_list':queryset,
		'title':"List View"
	}
	return render(request, "post_list.html", context)

def posts_update(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.user != request.user:
		messages.success(request, "You don't have permission to edit someone else's post.")
		return HttpResponseRedirect(instance.get_absolute_url())

	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance.user = request.user
		instance.slug = slugify(instance.title)
		instance = form.save(commit=False)

		instance.save()
		messages.success(request, 'Your post has been updated!')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'title':instance.title,
		'instance':instance,
		'form':form}
	return render(request, 'post_form.html', context)

# def post_delete(request, slug=None):
# 	instance = get_object_or_404(Post, slug=slug)
#
# 	if instance.user != request.user:
# 		print("hmm")
# 		messages.success(request, "You don't have permission to delete someone else's post.")
# 		return HttpResponseRedirect(instance.get_absolute_url())
#
# 	instance.delete()
# 	messages.success(request, "Successfully Deleted")
# 	return redirect('posts:list')

@login_required
def post_delete(request, slug=None):
	obj = get_object_or_404(Post, slug=slug)
	if request.method == 'POST':
		if request.user == obj.user:
			obj.delete()
			messages.success(request, "Your post has been deleted.")
			return redirect('posts:list')
			#something
		else:
			messages.success(request, "You don't have permission to delete this post.")
			return redirect('posts:list')
	context = {
		'object':obj,
	}
	if request.user == obj.user:
		return render(request, 'posts/confirm_delete.html', context)
	else:
		messages.success(request, "You don't have permission to delete this post.")
		return redirect('posts:list')

def posts_search(request):

	query = request.GET.get('q')

	today = timezone.now().date()

	# queryset_list = Post.objects.active()
	# if request.user.is_staff or request.user.is_superuser:
	# 	queryset_list = Post.objects.all()
	# #queryset_list = Post.objects.all().order_by("-timestamp")

	if query:
		queryset_list = Post.objects.active()
		if request.user.is_staff or request.user.is_superuser:
			queryset_list = Post.objects.all()
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query) |
			Q(user__first_name__icontains=query) |
			Q(user__last_name__icontains=query)
			).distinct()


	# else:
	# 	queryset_list = Post.objects.none()


	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		'object_list':queryset,

	}


	return render(request, 'search.html', context)

def posts_detail(request, slug):
	# instace = Post.objects.get(id=3)

	instance = get_object_or_404(Post, slug=slug)
	if instance.draft or instance.publish > timezone.now().date():
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content)



	initial_data = {
		'content_type':instance.get_content_type,
		'object_id':instance.id
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
		messages.success(request, 'Your comment was added!')
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

	comments = instance.comments

	context = {
		'title':instance.title,
		'instance':instance,
		'share_string':share_string,
		'comments':comments,
		'comment_form':form,
	}

	return render(request, "post_detail.html", context)
