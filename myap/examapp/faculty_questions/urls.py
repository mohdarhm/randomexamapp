from django.urls import path
from . import views

app_name = 'faculty_questions'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('portal/', views.portal_view, name='portal'),
    path('get_concepts/', views.get_concepts, name='get_concepts'),
]