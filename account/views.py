from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import (
    RegistrationForm,
    EditProfleForm
)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    args = {'user': request.user}
    return render(request, 'home.html', args)


def register_view(request):
    # POST, if the request.method==POST
    # Otherwise None
    form = RegistrationForm(request.POST or None)
    # form is invalid if request.method == GET
    if form.is_valid():
        form.save()
        return render(request, 'base.html', {})

    args = {
        'form': form,
        'user': request.user
    }
    return render(request, 'account/register.html', args)


@login_required
def view_profile(request, username):
    # 'user' = Info of logged in user
    other_user = User.objects.get(username=username)
    args = {
        'user': request.user,
        'other_user': other_user
    }
    if username == request.user.username:
        args['is_same_user'] = True
    else:
        args['is_same_user'] = False
    return render(request, 'account/view_profile.html', args)


@login_required
def edit_profile(request, username):
    # POST, if the request.method == POST
    # Otherwise None
    form = EditProfleForm(request.POST or None, instance=request.user or None)
    # form is invalid if request.method == GET
    if form.is_valid():
        form.save()
        return redirect('profile')

    args = {
        'form': form,
        'user': request.user
    }
    if username == request.user.username:
        args['is_same_user'] = True
    else:
        args['is_same_user'] = False
    return render(request, 'account/edit_profile.html', args)


@login_required
def change_password(request):
    form = PasswordChangeForm(data=request.POST or None, user=request.user)

    if form.is_valid():
        form.save()
        # This function keeps the user logged in after changing password
        update_session_auth_hash(request, form.user)
        return redirect('profile')

    args = {
        'form': form,
        'user': request.user
    }
    return render(request, 'account/change_password.html', args)

