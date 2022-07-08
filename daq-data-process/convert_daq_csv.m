% ##############################
% ########## EDIT HERE #########
% ##############################

folder_name= 'test-matlab';
feat_list_loc = sprintf('%s/%s', folder_name, 'feat_list.txt');

% ##############################
% ##############################

field_list = fieldnames(elemData);
N = length(field_list);
feat_list = strings(1, length(field_list)); % init array of strings
for i = 1 : N
    % get feature name: string
    filename = sprintf('%s.csv', field_list{i});
    
    % write list of features into txt files
    feat_list(1, i) = filename;
    writematrix(feat_list, feat_list_loc)

    
    % write values into csv files (w/ corresponding name)
    filepath = sprintf('%s/%s', folder_name, filename);
    writematrix(getfield(elemData, field_list{i}), filepath)
    
    
end