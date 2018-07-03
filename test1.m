%I = imread('/home/chetan/adap_thresh/aproject/cropped_dataset/1.jpg');
I = imread('tshape.png');
%I = rgb2gray(I);
adpt1=adaptivethreshold(I,15,0.02,0);
val= adaptthresh(I, 0.01);
adpt2 = imbinarize(I,val);

imshowpair(adpt1, adpt2, 'montage');