from django.contrib.auth import login, tokens
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .forms import RegistrationForm, UserEditForm, UserProfileForm
from .token import account_activation_token
from .models import Profile
from blog.models import BlogPost

# Create your views here.
@login_required
def favourites_list(request):
    favourites = BlogPost.publiished.filter(favourites=request.user)
    return render(request, 'accounts/favourites.html', {"favourites": favourites})

@login_required
def add_favourite(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'section': 'profile'})

def accounts_registration(request):
    if request.method == "POST":
        registrationForm = RegistrationForm(request.POST)
        if registrationForm.is_valid():
            user = registrationForm.save(commit=False)
            user.email = registrationForm.cleaned_data['email']
            user.set_password(registrationForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('registration/activate_account.html', {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": account_activation_token.make_token(user)
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('Registration is successful, please activate your account through email')
    else:
        registrationForm = RegistrationForm()
    return render(request, 'registration/register.html', {'form': registrationForm})
    
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('login')
    else:
        return render(request, 'registration/activation_invalid.html')

@login_required
def edit(request):
    if request.method == "POST":
        user_edit_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_edit_form.is_valid() and profile_form.is_valid():
            user_edit_form.save()
            profile_form.save()
    else:
        user_edit_form = UserEditForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)
    return render(request, 'accounts/update.html', {"form": user_edit_form, "profile_form": profile_form})

@login_required
def delete_user(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        user.is_active = False
        user.save()
        return redirect('accounts:login')
    return render(request, 'accounts/delete.html')