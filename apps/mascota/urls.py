from django.conf.urls import url
from apps.mascota.views import index

from django.conf.urls import url
from apps.mascota.views import index

urlpatterns = [
    url(r'^$', index),
]
