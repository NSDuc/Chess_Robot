function [c, selc, posX, posY, openbw, src] = catchroi(src)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
load camera;
src = undistortImage(src,cameraParams);
im = im2double(src);
[height,width,~] = size(im);
b = im(:,:,3);
r = im(:,:,1);
g = im(:,:,2);
Recognition = 0.1 *r+ 0.1 *g+ 0.8 *b;
%b = im(:,:,3);
%Recognition = b;

level = graythresh(Recognition);
%bw = im2bw(Recognition,level*0.78);
bw = im2bw(Recognition,level*0.72);
bw = imcomplement(bw);
se = strel('disk',2);
openbw=imclose(bw,se);

stats = regionprops(openbw, 'basic');

c = cat(1,stats.BoundingBox);
selc = find(abs(c(:,3) - c(:,4)) <= 20 & c(:,3) >= 75 & c(:,3) <= 120);
%assignin('base','c',c);
%assignin('base','y',y);

center = cat(1,stats.Centroid);
center = fix(center(selc,:));

for i = 1:size(selc);
    if c(selc(i),3) - (center(i,1) - c(selc(i),1))*2 > 5
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


%{
regionXb = c(selc,1);
regionXe = c(selc,1) + c(selc,3);
regionYb = c(selc,2);
regionYe = c(selc,2) + c(selc,4);

for i=1:size(selc)
    eval(['roi',num2str(i),'= src(regionYb(',num2str(i),'):regionYe(',num2str(i),...
        '),regionXb(',num2str(i),'):regionXe(',num2str(i),'),:);'])
    eval(['assignin(''base'',''roi'',roi',num2str(i),');'])
end
%}
%for i=1:size(selc)
%    roi = roi1;
%end
%roi = roi1;
posX = center(:,1);
posY = center(:,2);

%roi = src(regionYb:regionYe,regionXb:regionXe,:);
%posX = c(y,1) + c(y,3) * 0.5;
%posY = c(y,2) + c(y,4) * 0.5;
%assignin('base','roi',roi);

end