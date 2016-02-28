import numpy as np
import cv2
from queries import LabelDetection as ld

img = cv2.imread(filename)

def read(filename):
	result = ld.main(filename)
	authorize(result)
	