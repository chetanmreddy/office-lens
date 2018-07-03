I = imread('/home/chetan/adap_thresh/aproject/cropped_dataset/1.jpg');
I = rgb2gray(I);
I = double(I);

J = imgaussfilt(I,5.5) - imgaussfilt(I,1.5);
J = J - min(J(:));
J = J / max(J(:));


T = J > graythresh(J);

figure;
imshow(T);