function DrawMatch( Img1, m1, Img2, m2 )
%DRAWMATCH 
[x1, y1]=size(Img1);
[x2, y2]=size(Img2);
x = max(x1,x2);
Img = zeros(x,y1+y2);
Img(1:x1,1:y1)=Img1;
Img(1:x2,y1+1:y2+y1)=Img2;
figure;imshow(uint8(Img));
for n=1:length(m1)
hold on;
plot(m1(2,n),m1(1,n),'r+');
plot(y1+m2(2,n),m2(1,n),'r+');
S=[m1(2,n),y1+m2(2,n)];
T=[m1(1,n),m2(1,n)];
line(S,T);
end
hold off;

end