import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

images = os.listdir('gray')
imgname = np.random.choice(images, 1)[0]
img = cv2.imread('gray/'+imgname, cv2.IMREAD_GRAYSCALE)
img = cv2.bilateralFilter(img, 7, 50, 50)
edge = cv2.Canny(img, 20, 50)

'''
cv2.imshow('image', img)
while True:
    if cv2.waitKey(1)&0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
'''

plt.subplot(121)
plt.imshow(img, cmap = 'gray')

plt.title('Original Image')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(edge, cmap = 'gray')

plt.title('Edge Image')
plt.xticks([])
plt.yticks([])

plt.show()