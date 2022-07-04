% ##############################
% ######### START EDIT #########
% ##############################

folder_name= 'test-matlab_7-3';
feature_list_file = 'feat_list.txt';
data = elemData;
file_extension = '.txt';

% ##############################
% ########## END EDIT ##########
% ##############################

feat_list_loc = sprintf('%s/%s', folder_name, feature_list_file);
field_list = fieldnames(data);
N = length(field_list);
feat_list = strings(1, length(field_list)); % init array of strings
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