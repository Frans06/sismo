
from webcam import Webcam
from ipcamera import Ipcam
from scipy import signal
#//from picamera2 import Picam
from encoder import Encoder, RTMP
import numpy as np
from skimage.measure import compare_ssim as ssim

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

if __name__ == "__main__":
    camera = Webcam()
    if camera.isConnected() :
        try:
            print("copying output")
            camera.start()
            while (True):
                image1 = camera.getFrame()
                image2 = camera.getFrame()
                cor = ssim(image1,image2)
                if cor<0.78:
                        print("gettingframe:   ",cor)
                #camera.show(image1)
        except (KeyboardInterrupt, SystemExit):
                print("exiting")
                camera.stop()
    else:
        print ("problems")
