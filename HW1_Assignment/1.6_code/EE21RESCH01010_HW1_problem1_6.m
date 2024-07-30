%''''''''''''''exercise1.6 HW1''''''''''''
% The code loads all the data from given text file
% And then converting it to string then cell array and then each character
% of file is compared with all lowercase alphabets
fid=fopen("inputfile_16.txt",'rt')
    Epmf=[];%creating a blank emperial pmf vector corresponding to each alphabet in file
         load_data=importdata('inputfile_16.txt')% loading all data (characters) into array load_data
                %load data will be cell array(1*1)
                    ksrr=load_data(:);% accessing all elements
                        count=0;% for counting no. of characters in tex file
                        ksrr=ksrr{:}; %reading each line from cell 
                        ksrr=[ksrr]%making array
                        text_char ='abcdefghijklmnopqrstuvwxyz' % testing array of aphabets(since my file contains all lowercase characters)
                        length_char=sum(ismember(ksrr,text_char))%if any alphabet of text file matches with lowercase array,then ismember returns 1
                                for k=1:prod(size(text_char))% loop for checking each and every alphabet of text file with lower case
                                     count=sum(ismember(ksrr,text_char(k)));%checking tex_char with characters of text file
                                     Epmf(k)=count/length_char % required emperical pmf vector(26 long length)
                                end
%identation is provided to properly understand the code xthat one script
%conatins these many commands