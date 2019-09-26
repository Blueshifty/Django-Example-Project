from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    path('profile', views.profile_view, name='profile'),
    path('logout', views.logout_view, name='logout'),
 ]
