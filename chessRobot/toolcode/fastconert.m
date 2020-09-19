clear all;
close all;
clc;
tic
img=imread('D:\nntest\testimg\test134_1.jpg'); 
imshow(img)

[m n]=size(img);
score=zeros(m,n);

t=60;   %?��
for i=4:m-3
    for j=4:n-3
        p=img(i,j);    
        %�B?1�A�o��Hp?���ߪ�16??��?
        pn=[img(i-3,j) img(i-3,j+1) img(i-2,j+2) img(i-1,j+3) img(i,j+3) img(i+1,j+3) img(i+2,j+2) img(i+3,j+1) ...
            img(i+3,j) img(i+3,j-1) img(i+2,j-2) img(i+1,j-3) img(i,j-3) img(i-1,j-3) img(i-2,j-2) img(i-3,j-1)];

        %�B?2
        if abs(pn(1)-p)<t && abs(pn(9)-p)<t
           continue; 
        end
        
        %�B?3     
        p1_5_9_13=[abs(pn(1)-p)>t abs(pn(5)-p)>t abs(pn(9)-p)>t abs(pn(13)-p)>t];
        if sum(p1_5_9_13)>=3
            ind=find(abs(pn-p)>t);
            %�B?4         
            if length(ind)>=9
                score(i,j) = sum(abs(pn-p));      
            end
        end
    end
end

%�B?5�A�D��j���A�}�B?�X�S��?
for i=4:m-3
    for j=4:n-3
        if score(i,j)~=0
            if max(max(score(i-2:i+2,j-2:j+2)))==score(i,j)               
                [img(i-3,j), img(i-3,j+1), img(i-2,j+2), img(i-1,j+3), img(i,j+3), img(i+1,j+3), img(i+2,j+2), img(i+3,j+1), ...
                 img(i+3,j), img(i+3,j-1), img(i+2,j-2), img(i+1,j-3), img(i,j-3), img(i-1,j-3), img(i-2,j-2), img(i-3,j-1)]= ...
                 deal(255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255);
            end
        end
    end
end
figure;
imshow(img);
toc