from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core import signing
from django.conf import settings

from .forms import LoginForm

COOKIE_SIGNER_SALT = "accounts.cookie.salt"
COOKIE_MAX_AGE = 7 * 24 * 60 * 60 

def _set_signed_cookie(response, key, value, max_age=COOKIE_MAX_AGE, httponly=True, secure=None, samesite="Lax"):

    signed = signing.dumps(value, salt=COOKIE_SIGNER_SALT)
    if secure is None:
        secure = settings.SESSION_COOKIE_SECURE
    response.set_cookie(key, signed, max_age=max_age, httponly=httponly, secure=secure, samesite=samesite)

def _get_signed_cookie(request, key, default=None):
    raw = request.COOKIES.get(key)
    if not raw:
        return default
    try:
        return signing.loads(raw, salt=COOKIE_SIGNER_SALT, max_age=COOKIE_MAX_AGE)
    except Exception:
        return default

def set_preference(request):

    next_url = request.POST.get("next") or request.GET.get("next") or reverse("accounts:dashboard")
    if request.method == "POST":
        theme = request.POST.get("theme_color", "light")
        language = request.POST.get("language", "en")
    else:
        theme = request.GET.get("theme", "light")
        language = request.GET.get("language", "en")

    response = HttpResponseRedirect(next_url)
    _set_signed_cookie(response, "theme_color", theme)
    _set_signed_cookie(response, "language", language)
    return response

def user_login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            remember = form.cleaned_data["remember_me"]

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if remember:
                    request.session.set_expiry(30 * 24 * 60 * 60)
                else:
                    request.session.set_expiry(0)
                return redirect("accounts:dashboard")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})

@login_required
def dashboard(request):
 
    theme = _get_signed_cookie(request, "theme_color", "light")
    language = _get_signed_cookie(request, "language", "en")
    return render(request, "accounts/dashboard.html", {"theme": theme, "language": language})

def user_logout(request):
    logout(request)
    response = redirect("accounts:login")
    response.delete_cookie("sessionid")
    return response
