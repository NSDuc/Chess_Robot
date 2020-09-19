clear;clc;
str1='D:\nntest\chess\new_red\ØX\'; str3='.jpg';
for k = 5402
    str2 = num2str(k);
    SC = [str1,str2,str3];
    i = imread(SC);
    %i = imresize(src,[180,180]);
    %i=imcomplement(i);
    [l,m] = size(i);
    for n = 4:4:356
        j=imrotate(i, n, 'bilinear', 'crop');
        imwrite(j, [str1, num2str(k+n/2), '.jpg'], 'quality', 100);
    end
end
%figure