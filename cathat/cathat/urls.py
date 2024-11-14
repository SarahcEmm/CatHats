from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catarticles/', include('catarticles.urls')),  # updated line
    path('about/', views.about),
    path('', views.homepage),
]