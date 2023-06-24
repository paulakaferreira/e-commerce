from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = 'customer'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('registration-success/', views.registration_success, name='registration_success'),
    path('login/', auth_views.LoginView.as_view(), name='login')
    # path('login/', include('django.contrib.auth.urls'))
    # path('login/', views.login, name='login')
    # Other URL patterns for the "customer" app can be added here
]
