import numpy as np
import scipy
import cv2

def assign_pixel(s, t, pix_vec, moving_avg, rows, col):
	#print(pix_vec[300:400]);
	for k in range(s, len(pix_vec)):
		avg = moving_avg[k-s];
		if(pix_vec[k] < avg*(100-t)/100):
			pix_vec[k] = 1;
		else:
			pix_vec[k] = 0;
	pix_vec = pix_vec * 255;
	#print(pix_vec[9000:10000]);
	return np.reshape(pix_vec,(rows, col));


def precise_mov_avg(pix_vec,s,t):
	mylist = pix_vec;
	S = s;
	cumsum, moving_aves = [0], []

	for n, x in enumerate(mylist, 1):  #index starts from 1
		cumsum.append(cumsum[n-1] + x)
		if n>=S:
			moving_ave = (cumsum[n] - cumsum[n-S])/S
			#can do stuff with moving_ave here
			moving_aves.append(moving_ave)

	#print(moving_aves);
	return moving_aves;



def initialize(x_data, pix_vec):
	s = int((1/8)*(x_data.shape[1]));
	t = 15;
	return s,t;


def main():
	img = cv2.imread('/home/chetan/adap_thresh/cropped_dataset/28.jpg',0); # here 0 says to read image in gray scale

	x_data = np.array(img);

	pix_vec = x_data.flatten();
	print(len(pix_vec));
	s,t = initialize(x_data, pix_vec)

	moving_avg = precise_mov_avg(pix_vec,s,t);
	print(len(moving_avg));
	output = assign_pixel(s, t, pix_vec, moving_avg, x_data.shape[0], x_data.shape[1]);

	#resize the image and window to fit screen

	screen_res = 1280, 720
	scale_width = screen_res[0] / img.shape[1]
	scale_height = screen_res[1] / img.shape[0]
	scale = min(scale_width, scale_height)
	window_width = int(img.shape[1] * scale)
	window_height = int(img.shape[0] * scale)

	cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('dst_rt', window_width, window_height)

	cv2.namedWindow('dst_rt2', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('dst_rt2', window_width, window_height)

	cv2.imshow('dst_rt',img);
	cv2.imshow('dst_rt2', np.array(output, dtype = np.uint8));
	cv2.imwrite('28_quick_adap_thresh_op.jpg', output);

	cv2.waitKey(0);
	cv2.destroyAllWindows();

if __name__ ==	"__main__":
	main()