from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import FormLogin


# Create your views here.
def index(request):
    form = FormLogin()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../dashboard')


    return render(request, 'loginView/login.html', {'form': form})


@login_required(login_url= settings.LOGIN_URL)
def dashboard(request):
    context = {
        'username' : 'reyhan'
    }
    return render(request, 'loginView/dashboard.html', context)

def logout_view(request):
    logout(request)
    request.session.flush()

    return redirect('/login/')
