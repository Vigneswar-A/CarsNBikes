from django.urls import path
from store import views
from django.conf.urls.static import static
from CarsNBikes import settings
urlpatterns = [
    path("", views.home),
    path("sell/", views.sell),
    path("buy/",views.buy)
] + static(settings.STATIC_URL)