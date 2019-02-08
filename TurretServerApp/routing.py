from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^camera/', consumers.SocketConsumer),
    url(r'^ws/', consumers.ClientConsumer)
]