
from django.urls import path
from leads import views

app_name = 'leads'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('leads_all/', views.lead_list, name='lead_list'),
    path('leads_create/', views.lead_create, name='lead_create'),
    path('<int:pk>/', views.lead_detail, name='lead_detail'),
    path('<int:pk>/update', views.lead_update, name='lead_update'),
]
