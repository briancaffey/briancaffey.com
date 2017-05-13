from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Subreddit
import json
from urllib.parse import quote

from .utils import graph_, path
# Create your views here.
def graph_view(request):
    context = {}

    sr1 = request.GET.get('sr1')
    if sr1:
        #sr1 = quote(sr1)
        sr1 = quote(sr1)
        print(sr1)

    sr2 = request.GET.get('sr2')
    if sr2:
        print(sr2)
        sr2 = quote(sr2)

    print(sr2)
    if sr1 and sr2:
        print(sr1)
        print(sr2)
        sr_one = Subreddit.objects.filter(name=sr1 + '\n').first()
        print(sr_one)
        sr_two = Subreddit.objects.filter(name=sr2 + '\n').first()
        print(sr_two)
        if sr_one and sr_two:
            print("happy")
            context['search_result'] = path(sr_one.name.strip('\n'), sr_two.name.strip('\n'))

    results = graph_()
    context['results'] = results
    return render(request, 'srgraph/srgraph.html', context)

def get_subreddits(request):
    print("starting")
    if request.is_ajax():
        q = request.GET.get('term', '')
        subreddits = Subreddit.objects.filter(name__icontains = q )[:20]
        print("Hmm")
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
