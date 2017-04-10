from django.shortcuts import render, redirect
from .models import ReadingMaterial
from .forms import ReadingMaterialForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def reading_list(request):

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
        'reading_list':reading_list
    }

    return render(request, 'readinglist/reading_list.html', context)

def delete_reading(request):

    obj = get_object_or_404

    context = {
        "item":obj,
        "reading_list":rea
    }

    return render(request, 'readinglist/confirm_delete.html', context)
