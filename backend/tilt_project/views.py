from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
from users.forms import CustomUserCreationForm
import json

# Create your views here.


@ensure_csrf_cookie
def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    age = request.session.get_expiry_date()

    return render(
        request,
        'index.html',
        context={
            "num_visits": num_visits,
            "is_user_authenticated": request.user.is_authenticated,
            "age": age
        }
    )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/signup")
