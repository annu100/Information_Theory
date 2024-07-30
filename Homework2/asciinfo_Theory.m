clc
close all
clear all
fid=fopen('file2.txt','r');
fid2=fopen('asciiCodes.txt');
read2=fread(fid2);

read=fread(fid);
k=length(read);
fprintf('length-%d',k);
fprintf('%s',read2)
B =sort(double(read2)) %= double([ 'a':'z']); % Create Bin Ranges
l=length(B)
Hcts2 = histc(read,B);                % Do Histogram Counts
CB = char(B);  % Character Bins
disp("Frequency of characters in txt File")
for k1 = 1:l                        % Output Table
    fprintf('%c-',CB(k1))
    fprintf('%d\n',Hcts2(k1))
end
