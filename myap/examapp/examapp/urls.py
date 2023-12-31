"""
URL configuration for examapp project.

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
from . import views
# from faculty_questions import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('h/', views.home,name='examportal'),
    path('student-login/', views.student_login_view, name='student-login'),
    path('',views.debughome, name='homepage'),
    path('about/',views.aboutme, name='about'),
    path('res/',views.resource, name='res'),
    path('faculty/', include('faculty_questions.urls')),
    path('result_summary', views.result_summary, name='result_summary'),
]
