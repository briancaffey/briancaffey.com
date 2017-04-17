from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import UserProfile
from django.contrib.auth.models import User
from friends.models import Friend
# Create your views here.




def friend_list(request):

    all_users = UserProfile.objects.all().exclude(user=request.user)
    context = {
            "all_users":all_users,
        }
    if request.user.is_authenticated():
        friend_object, created = Friend.objects.get_or_create(current_user=request.user.userprofile)
        if friend_object.users:
            friends = [friend for friend in friend_object.users.all() if friend != request.user.userprofile]
            context['friends'] = friends

    return render(request, 'friends/friends_list.html', context)


def add_or_remove_friends(request, username, verb):
    n_f = get_object_or_404(User, username=username)
    owner = request.user.userprofile
    new_friend = UserProfile.objects.get(user=n_f)

    if verb == "add":
        Friend.make_friend(owner, new_friend)
    else:
        Friend.remove_friend(owner, new_friend)
    return redirect("friends:friend-list")
