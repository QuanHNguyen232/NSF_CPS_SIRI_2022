
% INPUT:
%   *.daq: file to read data
%   *.mat: list of chosen features (variables)
%   folder_name: output folder location (folder must exist)
%   file_extension: extension of output file
%   data: variable name of daq data (will appear in Matlab after reading daq file)

% RETURNS:
%   feat_list.txt: contains list of all features (variables)
%   In folder_name: has N files. Each corresponds to a feature

% Future suggestion:
%   Choose all features exist in *.daq file. Then we can select them much easier with Pandas (for Python users)
%   Optimizing code so that it can export 1 file for the whole dataset
%   Find way to read all n *.daq files using loop


%%%% START EDIT HERE

folder_name= './P32/Driving SIM/Each-feat';
file_extension = '.txt';
data = elemData;

%%%% END EDIT HERE


feature_list_file = 'feat_list.txt';
% combine folder + output filename
feat_list_loc = sprintf('%s/%s', folder_name, feature_list_file);
% get list of all fields from data
field_list = fieldnames(data);
% get total number of fields
N = length(field_list);
% init array of strings
feat_list = strings(1, length(field_list));
for i = 1 : N
    % get feature name: string
    feat_name = field_list{i};
    
    % write list of features into txt files
    feat_list(1, i) = feat_name;
    writematrix(feat_list, feat_list_loc)
    
    % write values into files (w/ corresponding name)
    filename = sprintf('%s%s', field_list{i}, file_extension);
    filepath = sprintf('%s/%s', folder_name, filename);
    writematrix(getfield(elemData, field_list{i}), filepath)
    
end
fprintf('convert_daq_csv -- DONE\n')

% Clear all data
clear