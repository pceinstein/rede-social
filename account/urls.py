from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # view de login
    # path('login/', views.user_login, name='login'),

    # todos os urls para as views de autenticação abaixo 
    # podem ser substituídos pelos padrões de url 
    # para autenticação do Django, da seguinte maneira:
    # path('', include('django.contrib.auth.urls'))

    # views de autenticação
    # urls de login e logout
    path('login/',
         auth_views.LoginView.as_view(),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),
    path('', views.dashboard, name='dashboard'),

    # urls para alteração de senha
    path('password_change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    
    # urls para reiniciar a senha
    path('password_reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]