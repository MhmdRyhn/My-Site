from django.shortcuts import render, redirect
from account.forms import (
	RegistrationForm,
	EditProfleForm
)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
#----------------- End of import ----------------------#



def home_view(request):
	return render(request, 'home.html', {})



def register_view(request):
	# POST, if the request.method==POST
	# Otherwise None
	form = RegistrationForm(request.POST, None)
	# form is invalid if request.method == GET
	if form.is_valid():
		form.save()
		return render(request, 'base.html', {})

	args = {'form': form}
	return render(request, 'account/register.html', args)



def view_profile(request):
	# 'user' = Info of logged in user
	args = {'user': request.user}
	return render(request, 'account/view_profile.html', args)



def edit_profile(request):
	# POST, if the request.method == POST
	# Otherwise None
	form = EditProfleForm(request.POST or None, instance=request.user)
	# form is invalid if request.method == GET
	if form.is_valid():
		form.save()
		return redirect('view_profile')

	args = {'form': form}
	return render(request, 'account/edit_profile.html', args)



def change_password(request):
	form = PasswordChangeForm(data=request.POST or None, user=request.user)
	if form.is_valid():
		form.save()
		update_session_auth_hash(request, form.user)

	args = {'form': form}
	return render(request, 'account/change_password.html', args)


















# The blank lines above are for ease of "TYPING" in "EDITOR"
