import numpy as np
import scipy
import glob
import cv2

'''
Here in this i am trying to make multiple patches of the input image and apply first algo on each individual patch

'''
def recombine_image(output_image, cropped_images2, height, width, r, c):
	p = 0;

	for h in range(0, height, r):
		for w in range(0, width, c):
			output_image[h:h+r, w:w+c] = np.reshape(cropped_images2[p], (r, c));
			p+=1;

	return output_image;


def assign_pixel(s, t, pix_vec, moving_avg, r, c, cropped_images2):
	#print(pix_vec[300:400]);
	for k in range(s, len(pix_vec)):
		avg = moving_avg[k-s];
		if(pix_vec[k] < avg*(100-t)/100):
			pix_vec[k] = 1;
		else:
			pix_vec[k] = 0;
	pix_vec = pix_vec * 255;
	#print(pix_vec[9000:10000]);
	cropped_images2.append(pix_vec);
	
	return np.reshape(pix_vec,(r, c));



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

def make_image_patches(inp, patches):
	#img = cv2.imread('/home/chetan/adap_thresh/aproject/cropped_dataset/28.jpg',0); # here 0 says to read image in gray scale

	no_of_patches = patches;

	rows = inp.shape[0];
	cols = inp.shape[1];

	windowsize_r = int(rows / no_of_patches);
	windowsize_c = int(cols / no_of_patches);

	d = 0;
	patched_images = []
	for r in range(0, rows, windowsize_r):
		for c in range(0, cols, windowsize_c):
			window = inp[r:r+windowsize_r,c:c+windowsize_c];
			patched_images.append(window);
			filename = "patch_%d.jpg"%d
			cv2.imwrite(filename, window);
			d+=1;

	return patched_images;


def main():
	#inp = cv2.imread('/home/chetan/adap_thresh/aproject/cropped_dataset/3.jpg',0); # here 0 says to read image in gray scale
	a = 1;
	for pic in glob.glob("/home/chetan/adap_thresh/aproject/cropped_dataset/*.jpg"):
		inp = cv2.imread(pic, 0);
		patches = 4; #no of divisions per side
		
		cropped_images = make_image_patches(inp, patches);
		height = inp.shape[0];
		width = inp.shape[1];

		output_image = np.zeros((height,width), np.uint8);

		cropped_images2 = [];
		for i in range(0, len(cropped_images)):
			patch = cropped_images[i];
			x_data = np.array(patch);

			pix_vec = x_data.flatten();
			#print(len(pix_vec));
			s,t = initialize(x_data, pix_vec)
			#print(s);
			moving_avg = precise_mov_avg(pix_vec,s,t);
			#print(len(moving_avg));
			output = assign_pixel(s, t, pix_vec, moving_avg, x_data.shape[0], x_data.shape[1], cropped_images2);


			#resize the image and window to fit screen
			'''
			screen_res = 1280, 720
			scale_width = screen_res[0] / patch.shape[1]
			scale_height = screen_res[1] / patch.shape[0]
			scale = min(scale_width, scale_height)
			window_width = int(patch.shape[1] * scale)
			window_height = int(patch.shape[0] * scale)
			'''
			#cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
			#cv2.resizeWindow('dst_rt', window_width, window_height)

			#cv2.namedWindow('dst_rt2', cv2.WINDOW_NORMAL)
			#cv2.resizeWindow('dst_rt2', window_width, window_height)

			#cv2.imshow('dst_rt',patch);
			#cv2.imshow('dst_rt2', np.array(output, dtype = np.uint8));

			#use this to see the patches ops

			#filename2 = "3_quick_adap_thresh2_op_patch_%i.jpg"%i   
			#cv2.imwrite(filename2, output);

			#cv2.waitKey(0);
			#cv2.destroyAllWindows();
		output_image = recombine_image(output_image, cropped_images2, height, width, x_data.shape[0], x_data.shape[1]);
		#cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
		#cv2.resizeWindow('dst_rt', window_width, window_height)
		#cv2.imshow('dst_rt', output_image);
		filename3 = "%a_op_quick_adap_thresh2.jpg"%a
		cv2.imwrite(filename3, output_image);
		#cv2.waitKey(0);
		#cv2.destroyAllWindows();
		a+=1;

if __name__ ==	"__main__":
	main()