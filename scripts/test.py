import sys
from os import listdir
from os.path import isfile, join

sys.path.append('../output/contour_detection-1.0-py3.9.egg')

import contour_detection

if __name__== "__main__":
    #acceptable true if contoured area > min percent, false if contoured area < min percent
    path = "../sample_images/test1.jpg"
    detection_obj = contour_detection.ContourDetection(path)
    acceptable = detection_obj.contoured_area(True)