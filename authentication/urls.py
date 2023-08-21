from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


app_name= "authentication"
urlpatterns = [
    path('', views.login_with_tokens, name='login'),
    path('redirect_after_login/', views.redirect_after_login, name='redirect_after_login')
]