import sys
import numpy as np
import os
import cv2

step = 5
h,s,v = 5,250,250

lower_range = np.array([h-step,s-step,v-step], dtype=np.uint8)
upper_range = np.array([h+step,s+step,v+step], dtype=np.uint8)

for (dir_path, dir_names, file_names) in os.walk(sys.argv[1]):
  for file_name in file_names:
    print file_name

    img = cv2.imread(os.path.join(sys.argv[1], file_name))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_range, upper_range)
    cv2.imwrite(os.path.join(sys.argv[2], file_name.split('.')[0]+'.png'), mask)
