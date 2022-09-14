from django.urls import path, reverse_lazy
from django.contrib.auth import views
from .views import UsuarioCreate

urlpatterns = [
    path('entrar/', views.LoginView.as_view(
        template_name='usuarios/login.html',
        extra_context={'titulo' : 'Autenticação'}
    ), name='login'),
    path('sair/', views.LogoutView.as_view(), name='logout'),
    path('alterar-minha-senha/', views.PasswordChangeView.as_view(
        template_name='usuarios/login.html',
        extra_context={'titulo' : 'Alterar senha atual'},
        success_url=reverse_lazy('index')
    ), name="alterar-senha"),
    path('registrar/', UsuarioCreate.as_view(), name='registrar')
]