clear;clc;
for num = 1:900
%num = 1;
k = 11700;
str1 = 'D:\nntest\chess\redmove_r\new\ØX\'; str4='.jpg';
str3 = num2str(num + k);
SC = [str1, str3, str4];
ia = imread(SC);
%inew = zeros(90, 90);
inew = im2double(ia);
inew(inew > 0.2) = 1;
inew(inew <= 0.2) = 0;
ss = 'D:\nntest\chess\sdepoint_r\ØX\';
imwrite(inew, [ss, num2str(num + k), '.jpg'], 'quality', 100);
end
%figure(1), imshow(ia);
%figure(2), imshow(inew);