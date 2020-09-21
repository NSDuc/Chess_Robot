load camera;
num = 184;
str1 = 'D:\nntest\testimg\'; str2 = 'Picture '; str4='.jpg';
str3 = num2str(num);
SC = [str1, str2, str3, str4];
src = imread(SC);
src = undistortImage(src,cameraParams);
src = im2double(src);

im = im2double(src);
[height,width,~] = size(im);
b = im(:,:,3);
r = im(:,:,1);
g = im(:,:,2);
Recognition = 0.1 *r+ 0.1 *g+ 0.8 *b;

radrange = 65;
Recognition2 = (Recognition(520:650,520:675))*255;
[accum, circen, cirrad] = CircularHough_Grd(Recognition2, [35, radrange]);
maxvalue = max(accum(:));
[x1, y1] = find(accum == maxvalue);
tx = x1+519; ty = y1+519;
%{
figure(1); imagesc(accum);
hold on
plot(ty, tx, 'g*')
t = [ty-40,tx-40,80,80]; 
rectangle('Position',t(1,:),'LineWidth',2,'LineStyle','--','EdgeColor','r'),
hold off
%}
src2 = src(520:650,520:675,:);
roi33 = src(tx-50:tx+49,ty-50:ty+49,:);
roi33 = im2uint8(roi33);
predictedLabel = ConvoNN(roi33);
figure(1),imshow(src2);
figure(2),imshow(roi33);title(char(predictedLabel))
