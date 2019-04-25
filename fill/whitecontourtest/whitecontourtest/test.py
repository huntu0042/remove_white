
"""
interval_upper_data.txt
image_name, interval, resized_interval
"""
import numpy as np
import scipy.io as sio
import cv2
def _load_image(img_name_dir):
  img = cv2.imread(img_name_dir)
  #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  return img


def main():
  interval_info = open("./interval_upper_data.txt").read().split()
  image_name = interval_info[0]
  interval = int(interval_info[1])
  resized_interval = int(interval_info[2])

  cloth_name = "_102014_1_"

  composition_raw = _load_image(image_name + cloth_name + "final.png")
  #composition_mask1 = cv2.imread(image_name + cloth_name + "mask.png", 0)

  cropped_image = composition_raw[:256, resized_interval:resized_interval + 192]
  
  cv2.imwrite("./1.png", cropped_image)
  """
  cv2.imshow('img', cropped_image)
  cv2.waitKey()
  cv2.destroyAllWindows()
  """
if __name__ == "__main__":
  main()    