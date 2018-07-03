clear;close all;
%im1=imread('page.png');
im2=imread('/home/chetan/adap_thresh/aproject/cropped_dataset/1.jpg');
im2=rgb2gray(im2);
%bwim1=adaptivethreshold(im1,11,0.03,0);
bwim2=adaptivethreshold(im2,15,0.02,0);%def is 15*15
%subplot(2,2,1);
%imshow(im1);
%subplot(2,2,2);
%imshow(bwim1);
%subplot(2,2,3);
%imshow(im2);
%subplot(2,2,4);
%imshow(bwim2);
imwrite(bwim2, '1_op_xiong_mean3.jpg');