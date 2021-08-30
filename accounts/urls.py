"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import delete_user, accounts_registration, activate, edit, add_favourite, favourites_list, like
from .forms import PwdResetConfirmForm, PwdResetForm, UserLoginForm, PasswordChangeForm

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html", authentication_form=UserLoginForm), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html", form_class=PwdResetForm), name='pwdreset'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html", form_class=PwdResetConfirmForm), name='pwdresetconfirm'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="registration/password_change_form.html", form_class=PasswordChangeForm), name='pwdchange'),
    path('edit/', edit, name='edit'),
    path('delete/', delete_user, name='delete_user'),
    path('favourites/', favourites_list, name='favourites_list'),
    path('like/', like, name='like'),
    path('fav/<int:id>/', add_favourite, name='add_favourite'),
    path('register/', accounts_registration, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]