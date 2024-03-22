from django.urls import path

from userauths import views as userauths_views
from store import views as store_views

urlpatterns = [
    path('user/token/', userauths_views.TokenObtainPairView.as_view(), name='Obtener Token'),
    path('user/registro/', userauths_views.RegisterView.as_view(), name='Registro Usuario')
]