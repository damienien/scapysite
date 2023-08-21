from django.urls import path
from . import views

app_name= "tickets"
urlpatterns = [
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('detail/<int:ticket_id>/', views.ticket_detail, name='detail'),
    path('', views.dashboard, name='dashboard'),
]