import numpy as np
import cv2

def img_fill(mask,img):

    dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
    return dst

img = cv2.imread('1_crop.png')
mask = cv2.imread('1_mask.png',0)

dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("fill_result.png", dst, [cv2.IMWRITE_PNG_COMPRESSION, 0])
 