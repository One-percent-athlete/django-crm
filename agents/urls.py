
from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailView

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agent_list'),
    path('agent_create/', AgentCreateView.as_view(), name='agent_create'),
    path('<int:pk>/', AgentDetailView.as_view(), name='agent_detail'),
]
