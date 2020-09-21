load camera;
num = 179;
str1 = 'D:\nntest\testimg\'; str2 = 'Picture '; str4='.jpg';
str3 = num2str(num);
SC = [str1, str2, str3, str4];
src = imread(SC);
src = undistortImage(src,cameraParams);

level = graythresh(src);
bw = im2bw(src,level);
bw = imcomplement(bw);
set_noise=500;
bw=bwareaopen(bw,set_noise);
[l,n] = bwlabel(bw,8);
figure(1),imshow(bw)
la1=(l*25);
la2=(l*10);
la3=(l*15);
lb=zeros(960,1280,3);
lb(:,:,1) = la1;
lb(:,:,2) = la2;
lb(:,:,3) = la3;
colorIm = gray2rgb('liftingbody.png','gantrycrane.png');

hold on
for k = 1:n
    [r,c]=find(l==k);
    rbar=mean(r);
    cbar=mean(c);
    plot(cbar,rbar,'Marker','*','MarkerEdgeColor','b','MarkerFaceColor','k','MarkerSize',10);
    %plot(cbar,rbar,'Marker','*','MarkerEdgeColor','w');
end
figure(2),image(cat(3,la1,la2,la3))