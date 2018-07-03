import numpy as np
import cv2

def recombine_image(output_image, patch, height, width, r, c):
	p = 0;

	for h in range(0, height, r):
		for w in range(0, width, c):
			output_image[h:h+r, w:w+c] = np.reshape(patch, (r, c));
			p+=1;

	return output_image;
def main():
	img = cv2.imread('/home/chetan/adap_thresh/aproject/cropped_dataset/1.jpg');

	height = img.shape[0];
	width = img.shape[1];

	#for pic in glob.glob("/home/chetan/MSR_OL/*.jpg"):
	output_image = np.zeros((height,width), np.uint8);

	#for i in range(0, 15):

	patch = cv2.imread('/home/chetan/MSR-OL/p0.jpg');
	#cv2.imshow('l', patch);
	r = patch.shape[0];
	c = patch.shape[1];
	print(r);
	print(c);
	op_img = recombine_image(output_image, patch, height, width, r, c);

	cv2.imshow('op', op_img);

	cv2.waitKey(0);
	cv2.destroyAllWindows();


if __name__ ==	"__main__":
	main()


