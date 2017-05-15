from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Subreddit, SearchResult
import json
from urllib.parse import quote
from datetime import datetime, timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .utils import path
# Create your views here.
def graph_view(request):


    sr1 = request.GET.get('sr1')
    if sr1:
        sr1 = quote(sr1)

    sr2 = request.GET.get('sr2')
    if sr2:
        sr2 = quote(sr2)

    if sr1 and sr2:
        sr_one = Subreddit.objects.filter(name=sr1 + '\n').first()
        sr_two = Subreddit.objects.filter(name=sr2 + '\n').first()

        if sr_one and sr_two:
            search_result = path(sr_one.name.strip('\n'), sr_two.name.strip('\n'))
            check = SearchResult.objects.filter(s_one=sr_one, s_two=sr_two)
            new_search_result = SearchResult(s_one=sr_one, s_two=sr_two, path=search_result['path'])

            print("OK1")
            if len(check) == 0:
                print("OK")
                sr = SearchResult(s_one=sr_one, s_two=sr_two, path=search_result['path'])
                sr.last_searched = datetime.now()
                sr.save()
            else:
                record = check.first()
                record.last_searched = datetime.now()
                record.save()

            # context['new_search_result'] = search_result

    previous_searches = SearchResult.objects.all()
    # context['previous_searches'] = previous_searches
    # numbers_list = range(1, 1000)
    page = request.GET.get('page', 1)
    paginator = Paginator(previous_searches, 20)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    # context['numbers'] = numbers

    # context['previous_searches'] = SearchResult.objects.all()
    return render(request, 'srgraph/srgraph_infinite_scroll.html', {'results':results})

def get_subreddits(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        subreddits = Subreddit.objects.filter(name__icontains = q )[:20]
        results = []
        for subreddit in subreddits:
            subreddit_json = {}
            subreddit_json['id'] = subreddit.name
            subreddit_json['label'] = subreddit.name
            subreddit_json['value'] = subreddit.name
            results.append(subreddit_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def get_random(request):
    if request.is_ajax():
        results = []
        random = Subreddit.objects.order_by('?')
        first_ = random.first().name.strip('\n')
        data = json.dumps(first_)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def view_result(request, id):

    result = SearchResult.objects.filter(pk=id).first()
    context = {'result':result,}

    return render(request, 'srgraph/view_result.html', context)


def upvote(request, id):

    result = SearchResult.objects.filter(pk=id).first()
    result.votes += 1
    result.save()
    return redirect('srgraph:srgraph')

def downvote(request, id):

    result = SearchResult.objects.filter(pk=id).first()
    result.votes -= 1
    result.save()
    return redirect('srgraph:srgraph')


def api_upvote(request, id):
    if request.is_ajax():
        result = SearchResult.objects.filter(pk=id).first()
        result.votes += 1
        result.save()
        total = result.votes
        data = json.dumps(total)
    else:
        data = 'fail'
    mimetype = 'appliction/json'
    return HttpResponse(data, mimetype)

def api_downvote(request, id):
    if request.is_ajax():
        result = SearchResult.objects.filter(pk=id).first()
        result.votes -= 1
        result.save()
        total = result.votes
        data = json.dumps(total)
    else:
        data = 'fail'
    mimetype = 'appliction/json'
    return HttpResponse(data, mimetype)

def popular(request):
    sr1 = request.GET.get('sr1')
    if sr1:
        sr1 = quote(sr1)

    sr2 = request.GET.get('sr2')
    if sr2:
        sr2 = quote(sr2)

    if sr1 and sr2:
        sr_one = Subreddit.objects.filter(name=sr1 + '\n').first()
        sr_two = Subreddit.objects.filter(name=sr2 + '\n').first()

        if sr_one and sr_two:
            search_result = path(sr_one.name.strip('\n'), sr_two.name.strip('\n'))
            check = SearchResult.objects.filter(s_one=sr_one, s_two=sr_two)
            new_search_result = SearchResult(s_one=sr_one, s_two=sr_two, path=search_result['path'])

            print("OK1")
            if len(check) == 0:
                print("OK")
                sr = SearchResult(s_one=sr_one, s_two=sr_two, path=search_result['path'])
                sr.last_searched = datetime.now()
                sr.save()
            else:
                record = check.first()
                record.last_searched = datetime.now()
                record.save()

            return redirect('srgraph:srgraph')

            # context['new_search_result'] = search_result

    previous_searches = SearchResult.objects.all().order_by('-votes')
    # context['previous_searches'] = previous_searches
    # numbers_list = range(1, 1000)
    page = request.GET.get('page', 1)
    paginator = Paginator(previous_searches, 20)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    # context['numbers'] = numbers

    # context['previous_searches'] = SearchResult.objects.all()
    return render(request, 'srgraph/srgraph_infinite_scroll_popular.html', {'results':results})

#
# def get_random(request):
#     if request.is_ajax():
#         results = []
#         random = Subreddit.objects.order_by('?')
#         first_ = random.first().name.strip('\n')
#         data = json.dumps(first_)
#     else:
#         data = 'fail'
#     mimetype = 'application/json'
#     return HttpResponse(data, mimetype)




#
