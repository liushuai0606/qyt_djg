"""qyt_djg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from views import index, qyt_template, qyt_forms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.qyt_index),
    path('summary', qyt_template.qyt_summary),
    path('sec', qyt_template.qyt_sec),
    path('dc', qyt_template.qyt_dc),
    path('addstudent', qyt_forms.addstudent),
    path('showstudents/', qyt_forms.showstudents),
    path('deletestudent/<int:id>', qyt_forms.deletestudent),
    path('editstudent/<int:id>', qyt_forms.editstudent),
]
