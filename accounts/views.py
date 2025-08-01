from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import  render

from accounts.forms import UserEditForm, ProfileEditForm
from accounts.models import Profile
from job.models import Jobs


def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')

def dashboard_view(request, username):
    user = get_object_or_404(User, username=username)
    jobs = Jobs.published.filter(author=user)
    profile = Profile.objects.filter(user=user).first()
    context = {
        'user':user,
        'jobs':jobs,
        'profile':profile
    }
    return render(request, 'dashboard.html', context)

def dashboard(request):
    user = request.user
    jobs = Jobs.published.filter(author=user)
    profile = Profile.objects.filter(user=user).first()
    context = {
        'user':user,
        'jobs':jobs,
        'profile':profile
    }
    return render(request, 'dashboard.html', context)


def edit_user(request):
    if request.method == "POST":
        user_form = UserEditForm(data=request.POST)
        profile_form = ProfileEditForm(data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('login')
    else:
        user_form = UserEditForm
        profile_form = ProfileEditForm
    context = {
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request, 'registration/profile_edit.html', context)