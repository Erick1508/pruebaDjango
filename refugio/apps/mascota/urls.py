from django.conf.urls import url
from refugio.apps.mascota.views import index

from django.conf.urls import url
from refugio.apps.mascota.views import index, mascota_view

urlpatterns = [
    url(r'^$', index, name= 'index'),
    url(r'^nuevo$', mascota_view, name= 'mascota_crear'),
]