from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # url de login
    # path('login/', views.user_login, name='login'),

    # todos as urls para as views de autenticação abaixo 
    # podem ser substituídas pelos padrões de url 
    # para autenticação do Django, da seguinte maneira:
    # path('', include('django.contrib.auth.urls'))

    ### urls de autenticação ###
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
     #####################################
     
     # url para registro de novo usuário
     path('register/', views.register, name='register'),

     # url para editar o perfil de usuário
     path('edit/', views.edit, name='edit'),

     path('users/', views.user_list, name='user_list'),
     path('users/follow/', views.user_follow, name='user_follow'),
     path('users/<username>/', views.user_detail, name='user_detail'),
]