from django.shortcuts import render, redirect
from django.contrib import messages  # Importez le module messages
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.utils.crypto import get_random_string
from .models import SessionToken
from django.contrib.auth.decorators import login_required

@login_required
def redirect_after_login(request):
    user = request.user
    if user.groups.filter(name='user').exists():
        return redirect(reverse('tickets:index'))
    else:
        return redirect(reverse('admin:index'))

def login_with_tokens(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            token = get_random_string(length=32)
            SessionToken.objects.create(user = user, token = token)
            print(user.groups.all())
            if user.groups.filter(name='user').exists() or user.groups.filter(name='expert').exists():
                return redirect(reverse('tickets:dashboard'))
            else:
                return redirect(reverse('admin:index'))
        else:
            messages.error(request, 'Identifiants incorrects. Veuillez réessayer.') 
            return render(request, 'login.html')
    return render(request, 'login.html')