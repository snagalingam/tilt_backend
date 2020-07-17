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


# @requires_csrf_token
# def register(request):
#     if request.method == 'POST':
#         body_data = json.loads(request.body)
#         email = body_data['email']
#         first_name = body_data['firstName']
#         # last_name = body_data['lastName']
#         password = body_data['password']
#         print(email)
#         print(first_name)


# def login_view(request):
#     username = request.POST['email']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return HttpResponseRedirect("/dashboard")
#     else:
#         return HttpResponseRedirect("/signup")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/signup")
