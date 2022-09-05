import numpy as np
import cv2
import matplotlib.pyplot as plt 
import os


folder = ".\segment"
for x in os.listdir(folder):
	if x[-1] == 'g':
		image = cv2.imread('images/'+x)
		print(x)
