
from django.urls import path
from leads import views
from .views import LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView, AssignAgentView

app_name = 'leads'

urlpatterns = [
    path('leads_all/', LeadListView.as_view(), name='lead_list'),
    # path('leads_all/', views.lead_list, name='lead_list'),

    path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    # path('<int:pk>/', views.lead_detail, name='lead_detail'),

    path('lead_create/', LeadCreateView.as_view(), name='lead_create'),
    # path('leads_create/', views.lead_create, name='lead_create'),
    path('<int:pk>/lead_assign_agent/', AssignAgentView.as_view(), name='lead_assign_agent'),

    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead_update'),
    # path('<int:pk>/update', views.lead_update, name='lead_update'),

    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead_delete'),
#     path('<int:pk>/delete', views.lead_delete, name='lead_delete'),
]
