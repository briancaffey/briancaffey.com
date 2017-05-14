from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Subreddit, SearchResult
import json
from urllib.parse import quote

from .utils import path
# Create your views here.
def graph_view(request):
    context = {}

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
            print("OK1")
            if len(check) == 0:
                print("OK")
                sr = SearchResult(s_one=sr_one, s_two=sr_two, path=search_result['path'])
                sr.save()

            context['search_result'] = search_result
    context['previous_searches'] = SearchResult.objects.all()
    return render(request, 'srgraph/srgraph.html', context)

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








#
