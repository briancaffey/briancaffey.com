from django.shortcuts import render, redirect
from .models import ReadingMaterial
from .forms import ReadingMaterialForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from tags.models import Tag

# Create your views here.

def reading_list(request):

    tags = Tag.objects.all()
    #tags = list(set([tag.tag for tag in tags]))
    form = ReadingMaterialForm(request.POST or None)
    reading_list = ReadingMaterial.objects.all()

    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.user = request.user

            instance.save()
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

def tag_view(request, id):
    tag = get_object_or_404(Tag, id=id)
    context = { "tag":tag }
    return render(request, 'readinglist/tag_view.html', context)
