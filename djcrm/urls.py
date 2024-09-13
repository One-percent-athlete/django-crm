from django.contrib import admin
from django.urls import path, include

# from leads.views import home_page
from leads.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('leads/', include('leads.urls', namespace='leads')),

]
