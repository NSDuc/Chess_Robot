clear;clc;
path = 'D:\nntest\chess\redmove_r\ØX_2\';
newpath = 'D:\nntest\chess\redmove_r\new\ØX\';
files = dir(strcat(path,'*.jpg'));
len=length(files);
for i=1:len
    oldname=files(i).name;
    newname=num2str(i+11880, '%i.jpg');
    old = strcat(path, oldname);
    new = strcat(newpath, newname);
    copyfile([path oldname],[newpath newname]);
end

