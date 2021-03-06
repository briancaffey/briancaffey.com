import requests
import feedparser


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_subscriptions(user):
    url = 'http://www.bucksamonth.com/api/v1/subscriptions/' + str(user)
    r = requests.get(url)
    subscriptions = r.json()
    return subscriptions


def get_blog_posts(number_of_posts):
    url = "http://briancaffey.github.io/feed"
    feed = feedparser.parse(url)
    posts = feed['items'][:number_of_posts]
    return posts
