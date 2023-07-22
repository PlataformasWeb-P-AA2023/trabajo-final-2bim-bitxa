from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import app.views as views

router = DefaultRouter()
router.register('personas', views.PersonaViewSet)
router.register('barrios', views.BarrioViewSet)
router.register('locales_comida', views.LocalComidaViewSet)
router.register('locales_repuestos', views.LocalRepuestoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('app.urls')),
]
