from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('leads.urls')),

    path('leads/', include('leads.urls', namespace='leads')),

]
