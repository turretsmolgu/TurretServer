from django.http import HttpResponse
from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .consumers import SocketConsumer
from .apps import TurretserverappConfig as tsc

# Create your views here.


def index(request):
    # channel_layer = get_channel_layer()
    # async_to_sync(channel_layer.group_send)(
    #     'my_group', 'from ger req'
    # )
    res = "!!! -> "
    if tsc.camera is None:
        res += 'no camera / '
        print('no camera')
    else:
        res += 'send to camera / '
        tsc.camera.send('from index to camera')

    if tsc.client is None:
        res += 'no client'
        print('no client')
    else:
        res += 'send to client'
        tsc.client.send('from index to client')
    return HttpResponse(res)


def test(request):
    return render(request, 'TurretServerApp/socket-test.html')

