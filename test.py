import cv2

#vcap = cv.VideoCapture("rtsp://192.168.100.128:554/profile2/media.smp")
#cap = cv2.VideoCapture("rtsp://192.168.100.128:554/profile2/media.smp")

# while(1):
#     ret, frame = vcap.read()
#     cv.imshow('VIDEO', frame)
#     cv.waitKey(1)

#while(True):
#    ret, img = cap.read()
#    cv2.imshow('img', img)
#    ch = cv2.waitKey(1)



from time import sleep
from picamera import PiCamera
import io
import librtmp
from subprocess import Popen, PIPE
import os

class BroadcastOutput(object):
	def __init__(self):
		self.streamer = Popen([ 
			'ffmpeg', 
			'-i', '-',
			'-vcodec', 'copy',
			'-an', 
			'-f', 'flv',
			'rtmp://demo.kawlantid.com/live/idiots'],
			stdin=PIPE, stderr=PIPE,
			shell=False, close_fds=True)

	def write(self, b):
		self.streamer.stdin.write(b)

	def flush(self):
		print("sejecuta")
		self.streamer.stdin.close()
		self.streamer.wait()

mystream = io.BytesIO()
camera = PiCamera()
camera.resolution = (640, 480)
output = BroadcastOutput()
print("copying  output")
camera.start_recording(output, format='h264')
# Create a connection
#conn = librtmp.RTMP("rtmp://demo.kawlantid.com/live/idiots", live=True)
# Attempt to connect
#conn.connect()
# Get a file-like object to access to the stream
#stream = conn.create_stream(mystream)
# Read 1024 bytes of data
#data = stream.read(1024)
print("injecting")
try:
	while True:
		print("wating")
		camera.wait_recording(1)
		print(output.streamer.stderr.read())
except KeyboardInterrupt:
	pass
finally:
	camera.stop_recording()
