from django.shortcuts import render, redirect
from .models import ReadingMaterial
from .forms import ReadingMaterialForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from taggit.models import Tag
import unidecode


# Create your views here.

def all_tags(request):
    tags = Tag.objects.all()
    context = {
        'tags':tags,
    }
    return render(request, 'readinglist/all_tags.html', context)

def tag_view(request, slug):
    tag = Tag.objects.get(slug=slug)
    stuff = ReadingMaterial.objects.filter(tags__name__in=[tag])
    context = {
        'tag':tag,
        'stuff': stuff,
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
            return redirect('reading-list:list')

        else:
            messages.success(request, "Please login to submit reading materials.")
            return redirect('reading-list:list')

    context = {
        'form':form,
        'reading_list':reading_list,
        'tags': tags

    }

    return render(request, 'readinglist/reading_list.html', context)

def delete_reading(request, slug):

    obj = get_object_or_404(ReadingMaterial, slug=slug)

    if request.method == "POST":
        obj.delete()
        return redirect('reading-list:list')

    context = {
        "item":obj,
    }


    return render(request, 'readinglist/confirm_delete.html', context)
