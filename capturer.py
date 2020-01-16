import os
import time
import numpy as np
import cv2
from mss import mss
from PIL import Image

class Capturer:
    def __init__(self):
        # create the directory to put the capturing data
        try:
            if os.path.exists('./capture'):
                if not os.path.isdir('./capture'):
                    print('You cannot have a file named "capture" in the directory!')
                    quit(1)
            else:
                os.mkdir('./capture')
            if os.path.exists('./gray'):
                if not os.path.isdir('./gray'):
                    print('You cannot have a file named "gray" in the directory!')
                    quit(1)
            else:
                os.mkdir('./gray')
        except:
            print('Cannot create captures directory.')
            quit(1)

        # the capture box to collect the data
        self.capture_box = {
            'top': 170,
            'left': 730,
            'width': 460,
            'height': 150
        }
        self.sct = mss()
    
    def __call__(self):
        return np.array(self.sct.grab(self.capture_box))
    
    def saveColor(self, imgname):
        if not self.img is None:
            pic = Image.fromarray(cv2.cvtColor(self.img, cv2.COLOR_BGRA2RGBA) , mode='RGBA')
            pic.save('capture/' + imgname)
    
    def saveGray(self, imgname):
        if not self.img is None:
            gimg = cv2.cvtColor(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2RGB)
            gpic = Image.fromarray(gimg, mode='RGB')
            gpic.save('gray/' + imgname)
    
    def run(self):
        while True:
            self.img = np.array(self.sct.grab(self.capture_box))
            cv2.imshow('screen', self.img)
            
            key = cv2.waitKey(1)
            if not key == -1:
                if (key & 0xff) == ord('c'):
                    imgname = str(time.time()).replace('.', '') + '.png'
                    self.saveColor(imgname)
                    self.saveGray(imgname)
                elif (key & 0xff) == ord('q'):
                    cv2.destroyAllWindows()
                    break

if __name__ == '__main__':
    cap = Capturer()
    cap.run()