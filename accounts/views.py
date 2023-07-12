from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserDetails
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from website.forms import ContactForm , PortfolioAdd , TestimonialAdd , ClientlogoAdd


def loginView(request):

    return render(request, 'users/login.html', {})

def signupView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account Created for {username} ! Please Log In and Add Your details.')
            return redirect('loginUrl')


    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    return render(request, 'users/signup.html', context)

@login_required
def profileView(request):

    context = {}
    return render(request, 'users/profile.html', context)

@login_required
def update_profileView(request):
    if request.method == 'POST':
        p_form = UserDetails(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Account sucessfully Updated for {request.user} !')
            return redirect('myaccountUrl')

    else:
        p_form = UserDetails(instance=request.user.profile)
    context = {
        'p_form': p_form
    }
    return render(request, 'users/updateprofile.html', context)

@login_required
def change_passwordView(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('myaccountUrl')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form
    }
    return render(request, 'users/changepassword.html', context)

@user_passes_test(lambda u: u.is_superuser)
def adminpanelActions(request):
    if request.method == 'POST':
        formPortf = PortfolioAdd(request.POST)
        if formPortf.is_valid():
            formPortf.save()
            messages.success(request, 'New Portfolio Item Addition Succeded!')
            return redirect('adminpanelactionsUrl')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        formPortf = PortfolioAdd(request.POST)

    if request.method == 'POST':
        formTesti = TestimonialAdd(request.POST)
        if formTesti.is_valid():
            formTesti.save()
            messages.success(request, 'New testimonial Item Addition Succeded!')
            return redirect('adminpanelactionsUrl')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        formTesti = TestimonialAdd(request.POST)

    if request.method == 'POST':
        formClilgo = ClientlogoAdd(request.POST)
        if formClilgo.is_valid():
            formClilgo.save()
            messages.success(request, 'New Portfolio Item Addition Succeded!')
            return redirect('adminpanelactionsUrl')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        formClilgo = ClientlogoAdd(request.POST)

    context = {
        'formTesti': formTesti,
        'formPortf': formPortf,
        'formClilgo': formClilgo
    }


    return render(request, 'users/adminconsole.html', context)