clc;
clear;
x=imread('/home/chetan/adap_thresh/aproject/cropped_dataset/15.jpg');
size(x);
x=imresize(x,[500 800]);
figure;
imshow(x);
title('original image');
z=rgb2hsv(x);       %extract the value part of hsv plane
v=z(:,:,3);
v=imadjust(v);
m = mean(v(:));
s=std(v(:));
k=-2;
value=m+ k*s;
temp=v;
for p=1:1:500
    for q=1:1:800
        pixel=temp(p,q);
        if(pixel>value)
            temp(p,q)=1;
        else
            temp(p,q)=0;
        end
    end
end
figure;
imshow(temp);
title('result by niblack');
% k=kittlerMet(g);
% figure;
% imshow(k);
% title('result by kittlerMet');

val2=m*(1+.1*((s/128)-1));
t2=v;
for p=1:1:500
for q=1:1:800
    pixel=t2(p,q);
    if(pixel>value)
        t2(p,q)=1;
    else
        t2(p,q)=0;
    end
end

end
figure;
imshow(t2);
title('result by sauvola');