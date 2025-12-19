from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
app_name = 'user'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_view, name='logout'),

]

