clear;clc;
for i = 1:4
    for num = 5401:5580
        %num = 1661;
        str1 = 'D:\nntest\chess\new_red\ØX\'; str4='.jpg';
        str3 = num2str(num);
        SC = [str1, str3, str4];
        ia = imread(SC);
        inew = zeros(90, 90);
        movex = 5;
        movey = 5;
        if i ==1
        inew(:,1+movey:90)=ia(:,1:90-movey); %rightmove
        k = 180;
        elseif i ==2
        inew(:,1:90-movey)=ia(:,1+movey:90); %leftmove
        k = 360;
        elseif i ==3
        inew(1:90-movex,:)=ia(1+movex:90,:); %upmove
        k = 540;
        else
        inew(1+movex:90,:)=ia(1:90-movex,:); %downmove
        k = 720;
        end
        inew = uint8(inew);
        ss = 'D:\nntest\chess\new_red\ØX\';
        imwrite(inew, [ss, num2str(num + k), '.jpg'], 'quality', 100);
    end
end
%figure(1), imshow(ia);
%figure(2), imshow(inew);
%}
%{
a = [1 2 3 4;5 6 7 8;9 10 11 12]
m = size(a);
b = zeros(m);
movex = 1;
movey = 2;
%b(:,movey+1:m(2)) = a(:,1:m(2)-movey) %rightmove
%b(:,1:m(2)-movey) = a(:,1+movey:m(2)) %leftmove
%b(1:m(1)-movey,:) = a(1+movey:m(1),:) %upmove
%b(1+movey:m(1),:) = a(1:m(1)-movey,:) %downmove
%}