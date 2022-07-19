#%%
import pandas as pd

#%%

# DATA generator
def daq_generator() -> pd.DataFrame:
    ''' Generate DataFrame from daq data
    Arguments:
        None

    Returns:
        df -- DataFrame of all partcipants from P1 -> P32. Save into "full-daq-dataset.txt" file
    '''

    df_lst = []
    for p_id in range(1, 33):
        filename = './P%d/P%d-merged_v2.txt'%(p_id, p_id)
        df_person = pd.read_csv(filename, sep='\t')
        df_lst.append(df_person)
    df = pd.concat(df_lst, axis=0)

    # check NaN values and drop
    print('df shape (before dropnan):', df.shape)
    print('total nan:', df.isna().sum().sum())
    df.dropna(axis=0, how='any', inplace=True)
    print('df shape (after dropnan):', df.shape)

    df.to_csv('./full-daq-dataset.txt', header=True, index=False, sep='\t', mode='a')

    print('df.shape', df.shape)
    return df

df = daq_generator()
#%%

def raw_eyetrk_generator() -> pd.DataFrame:
    ''' Generate DataFrame from eye-tracking data
    Arguments:
        None

    Returns:
        df -- DataFrame of all partcipants from P1 -> P32. Save into "full-raw-eyetrk-dataset.txt" file
    '''

    df_lst = []
    for p_id in range(1, 33):
        # no data from those Participants
        if p_id in {3, 20, 25, 32}: continue
        filename = './P%d/P%d-eyetrk_wind_label.txt'%(p_id, p_id)
        df_person = pd.read_csv(filename, sep='\t')
        df_lst.append(df_person)
    df = pd.concat(df_lst, axis=0)
    
    # check NaN values and drop
    print('df shape (before dropnan):', df.shape)
    print('total nan:', df.isna().sum().sum())
    df.dropna(axis=0, how='any', inplace=True)
    print('df shape (after dropnan):', df.shape)

    df.to_csv('./full-raw-eyetrk-dataset.txt', header=True, index=False, sep='\t', mode='a')

    # concatnate & return
    print('df.shape', df.shape)
    return df

df = raw_eyetrk_generator()

#%%
def combined_generator() -> pd.DataFrame:
    ''' Generate DataFrame from daq data
    Arguments:
        None

    Returns:
        big_df -- DataFrame of all partcipants from P1 -> P32. Save into "full-combined-dataset.txt" file
    '''

    eyetrk_list = []
    daq_list = []
    for p_id in range(1, 33):
        # no data from those Participants
        if p_id in {3, 20, 25, 32}: continue
        # Read eye-trking data
        df_eyetrk_file = './P%d/P%d-eyetrk_wind_label.txt'%(p_id, p_id)
        df_eyetrk = pd.read_csv(df_eyetrk_file, sep='\t')
        eyetrk_list.append(df_eyetrk)
        # Read daq data
        daq_file = './P%d/P%d-merged_v2.txt'%(p_id, p_id)
        df_daq = pd.read_csv(daq_file, sep='\t')
        daq_list.append(df_daq)

    # concatnate daq data 
    bigDF_eyetrk = pd.concat(eyetrk_list, axis=0)
    bigDF_eyetrk.drop(columns=['Label'], axis=1, inplace=True)
    bigDF_daq = pd.concat(daq_list, axis=0)
    if bigDF_eyetrk.shape[0] != bigDF_daq.shape[0]:
        raise Exception('daq and eyetrk DataFramse must have same number of rows')
    big_df = pd.concat([bigDF_daq, bigDF_eyetrk], axis=1)

    # check NaN values and drop
    print('big_df shape (before dropnan):', big_df.shape)
    print('total nan:', big_df.isna().sum().sum())
    big_df.dropna(axis=0, how='any', inplace=True)
    print('df shape (after dropnan):', big_df.shape)

    big_df.to_csv('./full-combined-dataset.txt', header=True, index=False, sep='\t', mode='a')

    # concatnate & return
    print('big_df.shape', big_df.shape)
    
    return big_df

df = combined_generator()


