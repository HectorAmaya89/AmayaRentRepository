
from django.urls import path
from AmayaRent import views



urlpatterns = [
    path('', views.inicio, name = "inicio"),
    # path('aptotemporales', views.AptoTemporales),
    path('quienes_somos', views.quienes_somos, name = "quienes_somos"),
    path('propiedades', views.propiedades, name = "propiedades"),
    path('contacto', views.contacto, name = "contacto"),
]
