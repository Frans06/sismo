import picamera
from camera import Camera
import io
import time
import os
from threading import Thread

class Picam(Camera):

    def __init__(self):
        super().__init__()
        resolution = tuple(self._configuration["resolution"])
        iso = self._configuration["iso"]
        video_stabilization = self._configuration["video_stabilization"]
        sharpness = self._configuration["sharpness"]
        exposure_compensation = self._configuration["exposure_compensation"]
        exposure_mode = self._configuration["exposure_mode"]
        meter_mode = self._configuration["meter_mode"]
        awb_mode = self._configuration["awb_mode"]
        image_effect = self._configuration["image_effect"]
        color_effects = self._configuration["color_effects"]
        rotation = self._configuration["rotation"]
        hflip = self._configuration["hflip"]
        vflip = self._configuration["vflip"]
        zoom = self._configuration["zoom"]

        self.camera = picamera.PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = self._framerate
        self.camera.sharpness = sharpness
        self.camera.contrast = self._contrast
        self.camera.brightness = self._brightness
        self.camera.saturation = self._saturation
        self.camera.ISO = iso
        self.camera.video_stabilization = video_stabilization
        self.camera.exposure_compensation = exposure_compensation
        self.camera.exposure_mode = exposure_mode
        self.camera.meter_mode = meter_mode
        self.camera.awb_mode = awb_mode
        self.camera.image_effect = image_effect
        self.camera.color_effects = color_effects
        self.camera.rotation = rotation
        self.camera.hflip = hflip
        self.camera.vflip = vflip
        self.camera.zoom = zoom
        self.stopped = False
        self._img = io.BytesIO()


    def start(self):
#        try:
#            self.t = Thread(target=self.update, args=())
#            self.t.daemon = True
#            self.t.start()
#        except Exception as e :
#            print("no se pudo guardar el frame", e)
        try:
            self.camera.start_recording(self.catcher, format = 'h264')
            time.sleep(1)
        except Exception as e :
            print("no se pudo guardar el video", e)


    def update(self):
        while self.stopped :
            self.camera.capture(self._img,format='bgr',use_video_port=True)

    def getFrame(self):
        return self._img

    def isConnected(self):
        try:
            self.camera.start_preview()
            time.sleep(2)
            self.camera.stop_preview()
            return True
        except Exception as e:
            print("error camera maybe is not connected", e)
            return False
            raise

    def defineH264(self,encoder):
        self.catcher = encoder

    def wait(self,time):
        self.camera.wait_recording(time)

    def stop(self):
        self.stopped = True
        self.camera.stop_recording()

