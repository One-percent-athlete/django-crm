from django.shortcuts import render, reverse
from django.core.mail import send_mail
from django.views import generic
import random

from leads.models import Agent
from .mixins import OrganizerLoginRequiredMixin
from .forms import AgentModelForm

class AgentListView(OrganizerLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = 'agents'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    
class AgentDetailView(OrganizerLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

class AgentCreateView(OrganizerLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent_list')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizer = False
        user.set_password(f'{random.randint(1, 10000000)}')
        user.save()
        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile
        )
        send_mail(
            subject='You are invited to be an agent.',
            message='Check your email to start to work as an agent with DJCRM',
            from_email='text@text.com',
            recipient_list=[user.email]
        )
        return super(AgentCreateView, self).form_valid(form)



class AgentUpdateView(OrganizerLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent_list')
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    

class AgentDeleteView(OrganizerLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agent_delete.html'

    def get_success_url(self):
        return reverse('agents:agent_list')
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

