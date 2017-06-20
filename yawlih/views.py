from django.shortcuts import render, redirect
from .models import Company, Investment, News
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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

@login_required
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

@login_required
def advanced_search(request):
    print("working")



    query = request.GET.get('q')
    print("query is: " + str(query))

    if query:
        all_companies = Company.objects.all()
        all_news = News.objects.all()
        all_investments = Investment.objects.all()

        results = all_companies.filter(
              Q(name_en__icontains=query) |
              Q(intro_en__icontains=query) |
              Q(intro_cn__icontains=query)
              ).distinct()
        news = all_news.filter(
            Q(headline__icontains=query) |
            Q(text__icontains=query)
            ).distinct()

        context = {
            'results': results,
            'news':news,
            'query': 'true'
        }
        return render(request, 'yawlih/reports.html', context)

    context = {
        'results':[],
        'query': 'false'
        }
    return render(request, 'yawlih/reports.html', context)

def user_logout(request):
    logout(request)
    return redirect('http://www.baidu.com/')
