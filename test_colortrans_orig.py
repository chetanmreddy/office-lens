from PIL import ImageFilter, Image
import numpy as np
import operator
import cv2
import os


img1 = cv2.imread('/home/chetan/adap_thresh/aproject/cropped_dataset/21.jpg')
img2 = cv2.imread('/home/chetan/MSR-OL/xing/adaptivethreshold/mean_median_ops/21_op_xiong.jpg')
rows,cols,dep = img1.shape
blank_image = np.ones((rows,cols,dep), np.uint8)
blank_image.fill(255)
p = []
q = []
img2 = np.invert(img2)
ret,img2 = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)
p,q,r = img2.nonzero()
for a,b in zip(p, q):
	blank_image[a,b] = img1[a,b]

blank_image = cv2.cvtColor(blank_image, cv2.COLOR_BGR2RGB)

height,width,channels = blank_image.shape

for i in range(height):
	for j in range(width):
		pixel = blank_image[i, j]
		#pixel.shape()
		if pixel[0] ==255 & pixel[1] ==255 & pixel[2] ==255:
			pixel[0] = 220
			pixel[1] = 220
			pixel[2] = 220
		index, value = max(enumerate(pixel), key=operator.itemgetter(1))
		#if pixel.all() < 250:
		#	pixel[0] = pixel[0]+pixel[0]*0.2
		#	pixel[1] = pixel[1]+pixel[1]*0.2
		#	pixel[2] = pixel[2]+pixel[2]*0.2
		if value!=220:
			value = value+value*0.1
			if value>255:
				value=255
		#	if pixel[0]>255:
		#		pixel[0]=255
		#	if pixel[1]>255:
		#		pixel[1]=255
		#	if pixel[2]>255:
		#		pixel[2]=255
		pixel[index] = value

blank_image = Image.fromarray(blank_image)

#cv2.namedWindow("output", cv2.WINDOW_NORMAL)
#imS = cv2.resize(blank_image, (0,0), fx=0.5, fy=0.5)
#blank_image = blank_image[:,:,::-1]
#cv2.imshow('output',imS)
#cv2.imwrite('op11.jpg',blank_image)
#blank_image.save('/home/chetan/MSR-OL/xing/adaptivethreshold/mean_median_ops_rgb/12_op_enhanced2','PNG')
blank_image.save('21_op_enhanced2','PNG')


k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()