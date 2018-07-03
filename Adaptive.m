%%%%%%%This algorithm works based on the premise that the background is
%%%%%%%more than the foreground in quantity as well as in intensity else
%%%%%%%invert the image

%%%%%% Adaptive  Thresholding 
 Image = imread('/home/chetan/adap_thresh/aproject/scripts/patch_16.jpg'); %%%%%For Image


% InputVideo = VideoReader('K:\\OCR\\VID_20170514_091047068.mp4');
% n          = InputVideo.NumberOfFrames
% Image = read(InputVideo,10);

height = size(image,1);
width  = size(image,2);
    
new_height = floor(height*640/width);
Image  = imresize(Image, [new_height, 640]);

% Image = rot90(rot90(rot90(Image)));
RGB   = imcrop(Image);
Image = rgb2gray(RGB);

%imtool(Image, [])

otsu_thresh = floor(graythresh(Image)*255);

percent = 100-(max(Image(:))- otsu_thresh);


Image = double(Image);
th_new = zeros(size(Image));
thresh_mat = zeros(size(Image));

division = floor(.1*size(Image,1));

s      = floor(size(Image,1)/8);
t      = 15;%double(max([percent,15]))
temp   = zeros(1,s);
thresh = 0;
count  = 0;
for i = 1 : size(Image,2)
    if(mod(i,2) == 0)
       start_point = size(Image,1);
       end_point = 1;
       step = -1;
    else
       start_point = 1;
       end_point = size(Image,1);
       step = 1;
    end
    for j = start_point:step:end_point
        
        thresh = running_average(Image(j,i),s, thresh, count);
        thresh_mat(j,i) = thresh;
        count = count + 1;
        
        if(i > 1)
            thresh = (thresh + thresh_mat(j,i-1))/2;
        end
        
        if(Image(j,i) < thresh*(100-t)/100)
            th_new(j,i) = 255;
        end
               
    end
end

imtool(uint8(th_new), [])