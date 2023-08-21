from django.shortcuts import render, redirect
from django.contrib import messages  # Importez le module messages
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.utils.crypto import get_random_string
from .models import SessionToken

# Create your views here.
def login_with_tokens(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request, user)
            token = get_random_string(length=32)
            SessionToken.objects.create(user = user, token = token)
            return redirect(reverse('polls:index'))
        else:
            messages.error(request, 'Identifiants incorrects. Veuillez réessayer.')  # Ajouter un message d'erreur
            return render(request, 'login.html')
    return render(request, 'login.html')