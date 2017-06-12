from django.shortcuts import render, redirect
from .models import Company, Investment
from django.contrib.auth.decorators import login_required

from django.contrib.auth import (
	logout,
	)


# Create your views here.
@login_required
def yl_home(request):
    companies = Company.objects.all()
    context = {
        'companies': companies,
    }
    return render(request, 'yawlih/yl_home.html', context)

def company_view(request, id):
    company = Company.objects.get(id=id)
    investments = Investment.objects.filter(company=company.id)
    context = {
        'company':company,
        'investments':investments,
    }
    return render(request, 'yawlih/company.html', context)


@login_required
def reports(request):
    return render(request, 'yawlih/reports.html', {})

def user_logout(request):
    logout(request)
    return redirect('http://www.yawlih.com.cn/')
