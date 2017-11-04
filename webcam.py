from camera import Camera
import cv2

class Webcam(Camera):
    def __init__(self):
        super(Webcam, self).__init__()
        frameWidth = self._configuration["width"]
        frameHeight = self._configuration["height"]
        exposure = self._configuration["exposure"]

        self.camera = cv2.VideoCapture(self._number)
        if not self.camera:
            raise Exception("Camera not accessible")
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHeight)
        self.camera.set(cv2.CAP_PROP_FPS, self._framerate)
        self.camera.set(cv2.CAP_PROP_BRIGHTNESS, self._brightness)
        self.camera.set(cv2.CAP_PROP_CONTRAST, self._contrast)
        self.camera.set(cv2.CAP_PROP_SATURATION, self._saturation)
        #self.camera.set(cv2.CAP_PROP_EXPOSURE, conf["exposure"])
        self.stopped = True
        (self._ret, self._img) = self.camera.read()
