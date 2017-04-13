from django.shortcuts import render, get_object_or_404, redirect
from .models import ReadingMaterial
from .forms import ReadingMaterialForm, ReadingMaterialUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from taggit.models import Tag
import unidecode
from django.contrib import messages
from django.conf import settings

#email
from django.core.mail import send_mail
EMAIL_HOST_USER = settings.EMAIL_HOST_USER


# Create your views here.

def view_item(request, pk):
    obj = ReadingMaterial.objects.get(pk=pk)
    context = {
        'obj':obj,
    }
    return render(request, 'readinglist/view_item.html', context)

def delete(request, pk):
    obj = ReadingMaterial.objects.get(pk=pk)
    if request.user == obj.user:
        obj.delete()
        return redirect('reading-list:list')
    else:
        messages.success(request, "You don't have permission to delete this.")
        return redirect('reading-list:list')


def all_tags(request):
    tags = Tag.objects.all()
    context = {
        # 'tags_':tags,
    }
    return render(request, 'readinglist/all_tags.html', context)

def tag_view(request, slug):
    tag = Tag.objects.get(slug=slug)
    stuff = ReadingMaterial.objects.filter(tags__name__in=[tag])
    count = len(stuff)
    context = {
        'tag':tag,
        'stuff': stuff,
        'count':count
    }


    return render(request, 'readinglist/tag_view.html', context)

def reading_list(request):


    #tags = list(set([tag.tag for tag in tags]))
    form = ReadingMaterialForm(request.POST or None)
    reading_list = ReadingMaterial.objects.all()
    tags = Tag.objects.all().distinct()



    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.user = request.user

            instance.save()
            # instance.tags.text = unidecode.unidecode(instance.tags)
            form.save_m2m()
            link = instance.link
            #send mail to admin
            messages.success(request, "Thanks for submitting a reading item to the list!")
            send_mail('[BRIANCAFFEY.COM] New reading suggestion from ' + str(request.user),
                'hmm', EMAIL_HOST_USER, [EMAIL_HOST_USER],
                html_message=str(request.user) + ' submitted a new item for reading. <br/>View it here: <a href="' + link + '">Link</a>')

            return redirect('reading-list:list')

        else:
            messages.success(request, "Please login to submit reading materials.")
            return redirect('reading-list:list')

    context = {
        'form':form,
        'reading_list':reading_list,
        'tags_': tags

    }

    return render(request, 'readinglist/reading_list.html', context)


def edit(request, pk):

    obj = get_object_or_404(ReadingMaterial, pk=pk)
    form = ReadingMaterialUpdateForm(request.POST or None, instance=obj)

    context = {
        'form':form,
        'obj':obj,
    }
    if form.is_valid():
        if request.user.is_authenticated():
            obj = form.save(commit=False)
            obj.user = request.user

            obj.save()
            # instance.tags.text = unidecode.unidecode(instance.tags)
            form.save_m2m()
            return redirect('reading-list:list')

        else:
            messages.success(request, "Please login to submit reading materials.")
            return redirect('reading-list:list')


    return render(request, 'readinglist/readinglist_edit.html', context)

# def delete_reading(request, slug):
#
#     obj = get_object_or_404(ReadingMaterial, slug=slug)
#
#     if request.method == "POST":
#         if request.user == obj.user:
#             obj.delete()
#             return redirect('reading-list:list')
#         else:
#             messages.success(request, "You don't have permission to delete this.")
#             return redirect('reading-list:list')
#
#     context = {
#         "item":obj,
#     }
#
#
#     return render(request, 'readinglist/confirm_delete.html', context)
