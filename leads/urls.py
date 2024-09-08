
from django.urls import path
from leads import views

app_name = 'leads'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('leads_all/', views.lead_list, name='lead_list'),
    path('leads/<str:pk>/', views.lead_detail, name='lead_detail'),
]
