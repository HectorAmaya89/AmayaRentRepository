
from django.urls import path
from AmayaRent import views



urlpatterns = [
    path('', views.inicio, name = "inicio"),
    # path('aptotemporales', views.AptoTemporales),
    path('aboutus', views.aboutus, name = "aboutus"),
    path('shop', views.shop, name = "shop"),
    path('contactus', views.contactus, name = "contactus"),
]
