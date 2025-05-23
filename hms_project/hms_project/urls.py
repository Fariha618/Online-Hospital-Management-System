"""
URL configuration for hms_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/login/', LoginView.as_view(template_name='registration/admin_login.html'), name='admin_login'),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url=reverse_lazy('admin_login')), name='root'),  # Redirect to login
    path('hospital/', include('hospital.urls')),  # app's URL patterns
    path('accounts/', include('django.contrib.auth.urls')),  # Django's auth URLs
    path('logout/', LogoutView.as_view(), name='logout'),
]