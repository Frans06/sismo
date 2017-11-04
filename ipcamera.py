import cv2
from camera import Camera
import os

class Ipcam(Camera):
    def __init__(self):
        super().__init__()
        _rtsp = self._configuration["rtsp"]
        self._ip = self._configuration["ip"]

        self.camera = cv2.VideoCapture("rtsp://192.168.100.128:554/profile2/media.smp")
# =============================================================================
#         if not self.camera:
#             raise Exception("Camera not accessible")
# =============================================================================
        self.stopped = True
        (self._ret, self._img) = self.camera.read()
    
    def isConnected(self):
        if os.system("ping -c 1 " + self._ip) == 0:
            return True
        else:
            return False
