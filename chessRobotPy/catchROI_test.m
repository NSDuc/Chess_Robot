clear; clc;
clearvars -except s; clc;
load camera;
num = 193;
str1 = 'C:\matlab code\testimg\'; str2 = 'Picture '; str4='.jpg';
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
%Recognition = 0.67*b;
%Recognition = b;
%figure(1),imshow(im)
%Recognition = gscale(Recognition,'full8');
%Recognition = intrans(Recognition,'stretch',mean2(im2double(Recognition)),2);
level = graythresh(Recognition);
%bw = im2bw(Recognition,level*0.78);
bw = im2bw(Recognition,level*0.62);
bw = imcomplement(bw);
se = strel('disk',2);
closebw=imclose(bw,se);
figure(1),imshow(src)
figure(3),imshow(Recognition)
figure(2),imshow(closebw)
%bw2 = imbinarize(Recognition,'adaptive','Sensitivity',0.5,'ForegroundPolarity','dark');


stats = regionprops(closebw, 'basic');
cc = regionprops(closebw, 'all');
%----------
%----------
c = cat(1,stats.BoundingBox);
selc = find(abs(c(:,3) - c(:,4)) <= 28 & c(:,3) >= 75 & c(:,3) <= 130);

center = cat(1,stats.Centroid);
center = fix(center(selc,:));
%{
for i = 1:size(selc);
    if (c(selc(i),3) - (center(i,1) - c(selc(i),1))*2) > 5
        c(selc(i),3) = c(selc(i),3) - (c(selc(i),3) - (center(i,1) - c(selc(i),1))*2) + 1;
    %elseif c(selc(i),3) - (c(selc(i),1) + c(selc(i),3) - center(i,1))*2 > 5
    %    c(selc(i),3) = c(selc(i),3) - (c(selc(i),3) - (c(selc(i),1) + c(selc(i),3) - center(i,1))*2) + 1;
    %    c(selc(i),1) = c(selc(i),1) + (c(selc(i),3) - (c(selc(i),1) + c(selc(i),3) - center(i,1))*2) - 1;
    end
end

for i = 1:size(selc);
    if c(selc(i),4) - (center(i,2) - c(selc(i),2))*2 > 5
        c(selc(i),4) = c(selc(i),4) - (c(selc(i),4) - (center(i,2) - c(selc(i),2))*2) + 1;
    %elseif c(selc(i),4) - (c(selc(i),2) + c(selc(i),4) - center(i,2))*2 > 5
    %    c(selc(i),4) = c(selc(i),4) - (c(selc(i),4) - (c(selc(i),2) + c(selc(i),4) - center(i,2))*2) + 1;
    %    c(selc(i),2) = c(selc(i),2) + (c(selc(i),4) - (c(selc(i),2) + c(selc(i),4) - center(i,2))*2) - 1;    
    end
end
%}
regionXb = c(selc,1);
regionXe = c(selc,1) + c(selc,3);
regionYb = c(selc,2);
regionYe = c(selc,2) + c(selc,4);
%figure(1),imshow(src)
%figure(2),imshow(closebw)
%}

hold on
plot(center(:,1), center(:,2), 'b*'),
for i=1:size(stats)
    if(c(i,3) >= 70 && c(i,4) >= 70)
        rectangle('Position',c(i,:),'LineWidth',2,'LineStyle','--','EdgeColor','r'),
    end
end
hold off

for i=1:size(selc)
eval(['roi',num2str(i),'= src(regionYb(',num2str(i),'):regionYe(',num2str(i),...
    '),regionXb(',num2str(i),'):regionXe(',num2str(i),'),:);'])
%figure(i+2)
%eval(['imshow(roi',num2str(i),')'])
%target = 'D:\nntest\testimg\';
%eval(['imwrite(roi',num2str(i),',[target,''test'',num2str(num),''_'',num2str(',num2str(i),'),''.jpg''],''quality'',100);'])
end
%}
