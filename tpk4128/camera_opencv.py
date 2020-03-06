import numpy as np
import cv2 as cv
import struct

#Due to some errors with cv2, I have to preload this.
import os
os.environ['LD_PRELOAD'] = '/usr/lib/arm-linux-gnueabihf/libatomic.so.1'


class Camera(object):

    def __init__(self):

        # Implement this constructor that opens a webcam and stores it in self._camera
        self._camera = cv.VideoCapture(0)
        if not self._camera.isOpened():
            print('Error opening camera.')
            exit()

    def capture(self):

        # Implement this function that grabs an image from the webcam and returns a numpy array
        ret, frame = self._camera.read()
        
        if not ret:
            print("Can't recieve frame. Exiting.")
            exit()
        
        greyimg = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
        img = struct.pack('ddd',greyimg)
        
        return img

    def __del__(self):

        # Implement this destructor. Remember to free the camera.
        self._camera.release()
        cv.destroyAllWindows()
    