import cv2
import json
from threading import Thread
import time

class Camera(object):
    def __init__(self):
        self._number = 1
        self._configuration = json.load(open("conf.json"))
        self._brightness = self._configuration["brightness"]
        self._contrast = self._configuration["contrast"]
        self._saturation = self._configuration["saturation"]
        self._framerate = self._configuration["framerate"]

    def show(self,img):
        try:
            cv2.imshow("test",img)
            cv2.waitKey(1)
        except Exception as e:
            print("error showing images",e)

    def start(self):
        self.t = Thread(target=self.update, args=())
        self.t.daemon = True
        self.t.start()
        return self

    def update(self):
        while self.stopped :
                (self._ret, self._img) = self.camera.read()

        #change to circular later pls :)

    def stop(self):
        self.stopped = False
        print("thread stopped")
        try:
            cv2.destroyAllWindows()
        except Exception as e:
            raise

    def getFrame(self):
        self._gray = cv2.cvtColor(self._img,cv2.COLOR_BGR2GRAY)
        return self._gray

    def isConnected(self):
        if (self.camera.open(self._number)):
            time.sleep(3)
            return True
        else:
            time.sleep(3)
            return False
