
from time import sleep
import io
from subprocess import Popen, PIPE
import os

class Encoder(object):
	def __init__(self,clase):
		self.convertion = clase()

	def write(self, b):
		self.convertion.process.stdin.write(b)

	def flush(self):
		self.convertion.process.stdin.close()
		self.convertion.process.wait()

class RTMP(object):
        def __init__(self):
            self.process = Popen([
                'ffmpeg',
                '-i', '-',
                '-vcodec', 'copy',
                '-an',
                '-f', 'flv',
                'rtmp://demo.kawlantid.com/live/idiots'],
                stdin=PIPE, stderr=PIPE,
                shell=False, close_fds=True)


#mystream = io.BytesIO()
#camera = PiCamera()
#camera.resolution = (640, 480)
#output = Encoder()
#print("copying  output")
#camera.start_recording(output, format='h264')



#print("injecting")
#try:
#        while True:
#                print("wating")
#                camera.wait_recording(1)
#                print(output.streamer.stderr.read())
#except KeyboardInterrupt:
#        pass
#finally:
#        camera.stop_recording()
