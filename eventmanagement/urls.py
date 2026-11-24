from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('services/', views.service, name='services'),
    path('event/', views.events, name='event'),
    path('contactus/', views.contact, name='contactus'),
    path('logout/', views.logout, name='logout'),
    path('planyourevent/', views.planyourevent, name='planyourevent'),
]