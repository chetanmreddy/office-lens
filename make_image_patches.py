import numpy as np
import scipy
import cv2

img = cv2.imread('/home/chetan/adap_thresh/aproject/cropped_dataset/1.jpg'); # here 0 says to read image in gray scale

no_of_patches = 4;

rows = img.shape[0];
cols = img.shape[1];

windowsize_r = int(rows / no_of_patches);
windowsize_c = int(cols / no_of_patches);

d = 0;
windows = []
for r in range(0, rows, windowsize_r):
	for c in range(0, cols, windowsize_c):
		window = img[r:r+windowsize_r,c:c+windowsize_c];
		windows.append(window)
		filename = "patch_%d.jpg"%d
		cv2.imwrite(filename, window);
		d+=1;

#for i in range(0, len(windows)):
#	cv2.imshow('img', windows[i]);

cv2.waitKey(0);
cv2.destroyAllWindows();
