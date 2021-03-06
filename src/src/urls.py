
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('frontend/', TemplateView.as_view(template_name='index.html'),),
    path('api/', include('api.urls')),
    
    path('', include('frontend.urls')),
    path('first/', include('first_app.urls')),
]
