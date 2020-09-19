function closeQ = redpreprocess(gray)

radrange = 45;
[accum] = CircularHough_Grd(gray, [radrange * 0.78, radrange]);
maxvalue = max(accum(:));
[x, y] = find(accum == maxvalue);

level=graythresh(gray);
bw = im2bw(gray,level);
se = strel('disk',2);
openbw = imopen(bw,se);
bw2 = imcomplement(openbw);

mask = ones(size(gray)) .* bw2;
mask = uint8(mask);
PP = gray .* mask;
t = linspace(0, 2*pi, 50);
r = 35;
c = [45 45];
BW = poly2mask(r*cos(t)+c(1), r*sin(t)+c(2), 90, 90);
Q = immultiply(PP,BW);

T = tabulate(Q(:));
T(1,:) = [];
[l,~] = size(T);
totalpercent = sum(T(:,3));
percent = 0;
for i = 1:l
    percent = percent + T(i,3);
    if percent > totalpercent * 0.66
        break
    end
end
th = T(i,1);
Q(Q > th) = 0;
Q(Q > 0) = 255;
closeQ = imclose(Q,se);
%{
if x > y
    mx = abs(x - 47);
    my = abs(y - 46);
else
    mx = abs(x - 46);
    my = abs(y - 47);
end
se = translate(strel(1),[mx my]); %[up_down left_right]
moveQ = imdilate(closeQ,se);
%}
end