from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('', views.home, name="home"),
    path('index/', views.index, name="index"),
    path('notification/', views.notification, name="notification"),
    path('information/', views.information, name="information"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
]    