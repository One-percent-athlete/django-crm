from django.contrib import admin
from django.urls import path, include

from leads.views import home_page, HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('leads.urls')),
    path('', HomePageView.as_view(), name='home'),

    path('leads/', include('leads.urls', namespace='leads')),

]
