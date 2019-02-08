from asgiref.sync import async_to_sync
from django.conf import settings

from channels.generic.websocket import WebsocketConsumer
from .apps import TurretserverappConfig as tsc


class SocketConsumer(WebsocketConsumer):

    def connect(self):
        # Join room group
        # async_to_sync(self.channel_layer.group_add)(
        #     'my_group',
        #     self.channel_name
        # )
        # print(self.channel_layer)
        self.accept()
        tsc.camera = self
        # TurretServerApp.apps.TurretserverappConfig.tempss.append(self)

    def receive(self, text_data=None, bytes_data=None):
        print('receive___Cam')
        print(text_data)
        # self.send('lol')

        print(bytes_data)

import cv2

class ClientConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        # tsc.tempss.append(self)
        tsc.client = self
        cap = cv2.VideoCapture(0)
        import time
        currentFrame = 0
        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Handles the mirroring of the current frame
            frame = cv2.flip(frame, 1)

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Saves image of the current frame in jpg file
            # name = 'frame' + str(currentFrame) + '.jpg'
            # cv2.imwrite(name, frame)

            # Display the resulting frame
            # cv2.imshow('frame', gray)
            # self.send({"type": "websocket.send", "bytes": gray})
            # l = len(bytearray(gray))
            ret, jpeg = cv2.imencode('.jpg', gray)
            self.send(bytes_data=jpeg.tobytes())
            time.sleep(0.1)
            # print(l)
            # print('------')
            # cv2.imwrite("frame%d.jpg" % currentFrame, frame)
            # data = bytearray(gray)

            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
            # if currentFrame == 20:
            #     break
            # To stop duplicate images

            # currentFrame += 1
        cap.release()

    def receive(self, text_data=None, bytes_data=None):
        print('receive___Cli')
        print(text_data)
        # self.send('lol')
        # for s in TurretServerApp.apps.TurretserverappConfig.tempss:
        #     s.send('lol')
        print(bytes_data)


