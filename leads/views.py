from typing import Any
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.views import generic
from agents.mixins import OrganizerLoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LeadForm, AssignAgentFrom,  LeadModelForm, CustomUserCreationForm, LeadCategoryUpdateForm
from .models import Lead, Agent, Category

class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')

class HomePageView(generic.TemplateView):
    template_name = 'home_page.html'

# def home_page(request):
#     return render(request, 'home_page.html')


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user

        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=False)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization, agent__isnull=False)
            queryset = queryset.filter(agent__user=user)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=True)
            context.update({
                'unassigned_leads': queryset
            })
        return context



# def lead_list(request):
#     leads = Lead.objects.all()

#     context = {"leads": leads}

#     return render(request, 'leads/lead_list.html', context)


class LeadDetailView(OrganizerLoginRequiredMixin, generic.DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'

# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)

#     context = {"lead": lead}

#     return render(request, 'leads/lead_detail.html', context)


class LeadCreateView(OrganizerLoginRequiredMixin, generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead_list')
    
    def form_valid(self, form):
        send_mail(
            subject='A lead has been created',
            message='Check your new lead',
            from_email='text@text.com',
            recipient_list=['test@test.com']
        )
        return super(LeadCreateView, self).form_valid(form)
    

# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('leads:lead_list')

    # context = {'form': form}
    # return render(request, 'leads/lead_create.html', context)

# def lead_create(request):
#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )
#             return redirect('leads:lead_list')

#     context = {'form': form}
#     return render(request, 'leads/lead_create.html', context)


class LeadUpdateView(OrganizerLoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead_list')
    
    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)
    

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect('leads:lead_list')

#     context = {
#         "lead": lead,
#         "form": form
#         }

#     return render(request, 'leads/lead_update.html', context)

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             lead.first_name=first_name,
#             lead.last_name=last_name,
#             lead.age=age,
#             lead.agent=agent
#             lead.save()
#             return redirect('leads:lead_list')

#     context = {
#         "lead": lead,
#         "form": form
#         }

#     return render(request, 'leads/lead_update.html', context)


class LeadDeleteView(OrganizerLoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')
    
    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)

# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect('leads:lead_list')


class LeadCategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/lead_category_update.html'
    form_class = LeadCategoryUpdateForm

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
        return queryset
    
    def get_success_url(self):
        return reverse('leads:category_list')
    

class AssignAgentView(OrganizerLoginRequiredMixin, generic.FormView):
    template_name = 'leads/lead_assign_agent.html'
    form_class = AssignAgentFrom

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({'request': self.request})
        return kwargs

    def get_success_url(self):
        return reverse('leads:lead_list')
    
    def form_valid(self, form):
        agent = form.cleaned_data['agent']
        lead = Lead.objects.get(id=self.kwargs['pk'])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)
    
class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/category_list.html'
    context_object_name = 'category_list'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user = self.request.user

        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)

        context.update({
            'unassigned_lead_count': queryset.filter(category__isnull=True).count()
        })

        return context

    def get_queryset(self):
        user = self.request.user

        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)
        return queryset
    
class CategoryDetailView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/category_detail.html'
    context_object_name = 'category' 

    def get_queryset(self):
        user = self.request.user

        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)
        return queryset
    
