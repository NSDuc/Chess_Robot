function [tx, ty] = turn_catch(src)
load camera;

src = undistortImage(src,cameraParams);
src = im2double(src);

im = im2double(src);
[height,width,~] = size(im);
b = im(:,:,3);
r = im(:,:,1);
g = im(:,:,2);
Recognition = 0.1 *r+ 0.1 *g+ 0.8 *b;

radrange = 65;
Recognition2 = (Recognition(560:700,470:620))*255;
[accum, circen, cirrad] = CircularHough_Grd(Recognition2, [35, radrange]);
maxvalue = max(accum(:));
[x1, y1] = find(accum == maxvalue);
tx = x1+559; ty = y1+469;
%{
figure(1); imagesc(accum);
hold on
plot(ty, tx, 'g*')
t = [ty-40,tx-40,80,80]; 
rectangle('Position',t(1,:),'LineWidth',2,'LineStyle','--','EdgeColor','r'),
hold off
src2 = src(500:650,550:700,:);
%}
%roi33 = src(tx-50:tx+49,ty-50:ty+49,:);
%figure(1),imshow(src2);
%figure(2),imshow(roi33);
