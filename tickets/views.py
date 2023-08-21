from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import TicketForm
from .models import Ticket, SharedTicket

# Create your views here.

@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'detail.html', {'ticket': ticket})
    

@login_required
def dashboard(request):
    user_tickets = Ticket.objects.filter(user = request.user)
    shared_tickets = SharedTicket.objects.filter(user = request.user)
    is_user = request.user.groups.filter(name='user').exists()
    context = { 'user_tickets': user_tickets, 'shared_tickets': shared_tickets, 'is_user': is_user }
    return render(request, 'dashboard.html', context)

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            # Envoie le ticket aux experts
            expert_group = Group.objects.get(name='expert')
            shared_ticket = SharedTicket.objects.create(ticket=ticket)
            shared_ticket.user.set(expert_group.user_set.all())
            
            return redirect('tickets:dashboard')  # Redirigez vers une page de confirmation
        else:
            # Gérer le cas où le formulaire n'est pas valide
            return render(request, 'create_ticket.html', {'form': form})
    else:
        form = TicketForm()

    return render(request, 'create_ticket.html', {'form': form})