from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from .models import *
from itertools import chain
# Create your views here.


def signUp(request):

    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.warning(request, 'email has already been taken')
                return redirect('sign-up')
            elif User.objects.filter(username = username).exists():
                messages.warning(request, 'username has already been taken')
                return redirect('sign-up')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                user.save()

                user_login = authenticate(username=username, password=password)
                login(request, user_login)

                # create profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.error(request, 'password does not match')
            return redirect('sign-up')
    else:
        return render(request, 'core/signup.html')

def signIn(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'core/signIn.html')

def home(request):
    user_object = User.objects.get(username=request.user.username)
    # user_profile = Profile.objects.get(user = user_object)
    if Profile.objects.filter(user = request.user).exists():
        user_profile = Profile.objects.get(user = user_object)
    else:
        user_profile = print('request.user does not exist')
    # user_profile = Profile.objects.all()

    userFollowings = []
    feed = []

    userFollowing = Follow.objects.filter(follower=request.user.username)

    for users in userFollowing:
        userFollowings.append(users.user)

    for usernames in userFollowings:
        feedLists = Post.objects.filter(user=usernames)
        feed.append(feedLists)

    feedList = list(chain(*feed))
    # posts = Post.objects.all()
    context = {'user_profile': user_profile, 'posts':feedList}
    return render(request, 'core/index.html', context)

def settings(request):

    if Profile.objects.filter(user = request.user).exists():
        user_profile = Profile.objects.get(user = request.user)
    else:
        user_profile = print('request.user does not exist')

    if request.method == 'POST':
        
        if request.FILES.get('profileImg') == None:
            profileImg = user_profile.profileImg
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileImg = profileImg
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        if request.FILES.get('profileImg') is not None:
            profileImg = request.FILES.get('profileImg')
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileImg  = profileImg
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        return redirect('settings')

    # edit_profile = ProfileForm(instance=request.user)

    # if request.method == 'POST':
    #     edit_profile = ProfileForm(request.POST, request.FILES, instance=request.user)

    #     if edit_profile.is_valid():
    #         edit_profile.save()
    #         return redirect('home')

    context = {'user_profile':user_profile}
    return render(request, 'core/settings.html', context)

def post(request):

    if request.method == 'POST':
        user = request.user.username
        files = request.FILES.get('files_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, files=files, caption=caption)
        new_post.save()

        return redirect('home')
    else:
        return redirect('home')
    
    # context = {'new_post': new_post}
    # return render(request, 'core/index.html', context)
        
def likePost(request):
    
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(username=username, post_id=post_id).first()

    if like_filter == None:
        newLike = LikePost.objects.create( post_id=post_id, username=username)
        newLike.save()

        post.no_of_likes = post.no_of_likes + 1
        post.save()
        return redirect('home')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes - 1
        post.save()
        return redirect('home')
    
def profilePage(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_profile_posts = Post.objects.filter(user = user_object)
    user_post_length = len(user_posts)

    follower = request.user.username
    user = pk 

    if Follow.objects.filter(follower=follower, user=user).first():
        buttonText = 'unfollow'
    else:
        buttonText = 'follow'

    userFollowers = len(Follow.objects.filter(user=pk))
    userFollowing = len(Follow.objects.filter(follower=pk))

    context = {'user_object':user_object, 'user_profile':user_profile, 'user_posts':user_posts, 'user_post_length':user_post_length, 'buttonText':buttonText, 'userFollowers':userFollowers, 'userFollowing':userFollowing, 'user_profile_posts':user_profile_posts}
    return render(request, 'core/profile.html', context)

def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if Follow.objects.filter(follower=follower, user=user).first():
            unFollow = Follow.objects.get(follower=follower, user=user)
            unFollow.delete()
            return redirect('profile/'+user)

        else:
            follow = Follow.objects.create(follower=follower, user=user)
            follow.save()
            return redirect('profile/'+user)
        
    else:
        return redirect('home')

def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user= user_object)

    if request.method == 'GET':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profileList = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profileList.append(profile_lists)

        username_profileList = list(chain(*username_profileList))

    return render(request, 'core/search.html', {'username_profileList':username_profileList})
