# import pyqrcode
# import png
# import QRcode
# a="https://www.python.org/downloads/"
# qrcode=pyqrcode.create(a)
# qrcode.svg("myqr.svg",scale=12)
# qrcode.png("myqr.png",scale=10, module_color=[1,0,0], background=[0,0,0])
import numpy as np
import imageio
import scipy.ndimage
import cv2
# take image input and assign into sketch
img="akash.jpeg"
# function to convert image into sketch
def rgb2grey(rgb):
    # 2 dimentional array to convert image to sketch
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])
def dodge(front, back):
    # if image is greater than 255(which is not possible) it will convert it to 255
    final_sketch=front*255/(255-back)
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    # to convert any suitable existing column to categorical type we will use aspect function
    # uint8 is for 8-bit signed integer
    return final_sketch.astype('uint8')
ss= imageio. imread(img)
gray=(ss)
i=255-gray
# to convert into a blur image
blur=scipy.ndimage.filters.rank_filter(i, sigma=13)
# calling the function
r=dodge(blur, gray)
cv2.imwrite('4.png',r)