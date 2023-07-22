from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('', views.home, name='home'),
    
    # Urls para Barrio
    path('listar_barrios/', views.listar_barrios, name='listar_barrios'),
    path('crear_barrio/', views.crear_barrio, name='crear_barrio'),
    path('editar_barrio/<int:id>/', views.editar_barrio, name='editar_barrio'),
    path('borrar_barrio/<int:id>/', views.borrar_barrio, name='borrar_barrio'),

    # Urls para Persona
    path('listar_personas/', views.listar_personas, name='listar_personas'),
    path('crear_persona/', views.crear_persona, name='crear_persona'),
    path('editar_persona/<int:id>/', views.editar_persona, name='editar_persona'),
    path('borrar_persona/<int:id>/', views.borrar_persona, name='borrar_persona'),

    # Urls para LocalRepuesto
    path('listar_locales_repuestos/', views.listar_locales_repuestos,
         name='listar_locales_repuestos'),
    path('crear_local_repuesto/', views.crear_local_repuesto,
         name='crear_local_repuesto'),
    path('editar_local_repuesto/<int:id>/',
         views.editar_local_repuesto, name='editar_local_repuesto'),
    path('borrar_local_repuesto/<int:id>/',
         views.borrar_local_repuesto, name='borrar_local_repuesto'),

    # Urls para LocalComida
    path('listar_locales_comida/', views.listar_locales_comida,
         name='listar_locales_comida'),
    path('crear_local_comida/', views.crear_local_comida,
         name='crear_local_comida'),
    path('editar_local_comida/<int:id>/',
         views.editar_local_comida, name='editar_local_comida'),
    path('borrar_local_comida/<int:id>/',
         views.borrar_local_comida, name='borrar_local_comida'),
]
