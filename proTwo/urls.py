"""proTwo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path
from AppTwo import views
=======
from django.urls import path, include
#
# from django.conf.urls import url, include
# from django.contrib import admin
# from django.urls import path
from first_app import views
>>>>>>> 5607d8f0c02b4ddfa2ad72cac94c6966158ab5b3

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path("temp/", include('first_app.urls')),
    #path("test/", views.test_template, name="template"),
]
