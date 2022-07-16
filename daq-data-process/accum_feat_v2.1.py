# %%
import pandas as pd

# %%
def accum_feat(target_folder: str, out_name: str, data_extension='txt') -> None:
    """
    Merge each feature data file into a big dataset since each feature is exported as a seperate file from convert_daq-txt-csv.m (Matlab)
    
    Arguments:
        target_folder -- location folder of list of feature .txt files
        out_name -- file name of output file (expect .txt file)
        data_extension -- OPTIONAL: file extension of those feature data file (expect: .txt as results from convert_daq_txt.m)
    
    Returns:
        None -- create a merged dataset named 'out_name'
    """

    with open(target_folder + '/feat_list.txt', 'r') as f:
        # Read all features
        feat_list = f.readline().replace('\n', '').split(',')
        # Read all csv files
        df_list = [pd.read_csv('%s/%s.%s'%(target_folder, feat, data_extension), header=None, prefix=feat) for feat in feat_list]
        # Concatnate all df into 1 df
        df = pd.concat(df_list, axis=1)
        # check nan
        x=7 # 28 feats
        print(df.isna().sum()[:x*1])
        print(df.isna().sum()[x*1:x*2])
        print(df.isna().sum()[x*2:x*3])
        print(df.isna().sum()[x*3:x*4])
        print(df.isna().sum().sum())
        print(df.tail(5)['Frames0'], df.shape)
        # Save df as file
        if df.isna().sum().sum() == 0:
            df.to_csv(out_name, header=True, index=False, sep='\t', mode='a')
        else:
            print('Missing values (NaNs)')
            return False
        
        
    print('accum_feat func -- concat and create {%s} -- DONE'%(out_name))
    return True

# %%
if __name__ == '__main__':
    
    num_samples = 2

    for p_id in range(1, num_samples):
        
        # START EDIT
        target_folder = './P%d/Driving SIM/Each-feat'%(p_id)
        out_file = './P%d/P%d-daq.txt'%(p_id, p_id)
        # END EDIT

        if not accum_feat(target_folder, out_file):
            break

        print(target_folder, out_file)

    
    print('accum_feat.py -- DONE')
    
