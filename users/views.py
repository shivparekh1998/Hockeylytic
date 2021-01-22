from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, UserTypeForm, UserDeleteForm
from django.contrib.auth.decorators import login_required
from functions import find_special_chars


# Form for registration page
def register(request):
    while True:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            type_form = UserTypeForm(request.POST)
            if find_special_chars(request.POST['first_name']) == True or \
                    find_special_chars(request.POST['last_name']) == True:
                messages.error(request, 'Please enter a valid first and last name')
                break
            if form.is_valid() and type_form.is_valid():
                # Need to do it this way to create the profile instance
                user = form.save()
                user.refresh_from_db()
                profile_form = UserTypeForm(request.POST, instance=user.profile)
                profile_form.full_clean()
                profile_form.save()
                messages.success(request, f'Your account has been created! Please login.')
                return redirect('login')
            break
        else:
            form = UserRegisterForm()
            type_form = UserTypeForm()
            break

    context = {
        'form': form,
        'type_form': type_form,
    }
    return render(request, 'users/register.html', context)


# Form for updating profile
@login_required
def profile(request):
    while True:
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            if find_special_chars(request.POST['first_name']) == True or \
                    find_special_chars(request.POST['last_name']) == True:
                messages.error(request, 'Please enter a valid first and last name')
                break
            if u_form.is_valid():
                u_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')
            break
        else:
            u_form = UserUpdateForm(instance=request.user)
            break

    context = {
        'u_form': u_form,
    }

    return render(request, 'users/profile.html', context)


# View for deleting user from account settings
@login_required
def account_settings(request):
    if request.method == 'POST':
        form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.success(request, f'Your account has been deleted')
        return redirect('home')
    else:
        form = UserDeleteForm(instance=request.user)

    context = {
        'title': 'Account Settings',
        'form': form,
    }

    return render(request, 'users/account_settings.html', context)
