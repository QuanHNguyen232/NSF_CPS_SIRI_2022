#
import pandas as pd
import numpy as np
from typing import List

#
def window_calculate(df: pd.DataFrame, label:str, window_size:int, methods=['mean', 'median', 'std']) -> pd.DataFrame:
    print(df.shape)
    df_label = df[df['Label']==label]
    df_label = df_label.groupby(np.arange(len(df_label.index)) // window_size)[df_label.columns].agg(methods)
    df_label['Label'] = label
    return df_label

# DATALOADER
def daq_dataloader(features: List, window_size=30) -> pd.DataFrame:
    df_lst = []
    for p_id in range(1, 33):
        filename = '../P%d/P%d-merged_v2.txt'%(p_id, p_id)
        df_person = pd.read_csv(filename, sep='\t')
        df_lst.append(df_person)
    df = pd.concat(df_lst, axis=0)
    df = df[features]

    # check NaN values and drop
    print('df shape (before dropnan):', df.shape)
    print('total nan:', df.isna().sum().sum())
    df.dropna(axis=0, how='any', inplace=True)
    print('df shape (after dropnan):', df.shape)

    df_lst_2 = []
    for label in ('tire', 'construct', 'rain', 'deer'):
        df_lst_2.append(window_calculate(df, label, window_size))

    # concatnate & return
    df_wind = pd.concat(df_lst_2, axis=0)
    print('df_wind.shape', df_wind.shape)
    return df_wind

def raw_eyetrk_dataloader(features: List, window_size=30) -> pd.DataFrame:
    df_lst = []
    for p_id in range(1, 33):
        # no data from those Participants
        if p_id in {3, 20, 25, 32}: continue
        filename = '../P%d/P%d-eyetrk_wind_label.txt'%(p_id, p_id)
        df_person = pd.read_csv(filename, sep='\t')
        df_lst.append(df_person)
    df = pd.concat(df_lst, axis=0)
    df = df[features]
    
    # check NaN values and drop
    print('df shape (before dropnan):', df.shape)
    print('total nan:', df.isna().sum().sum())
    df.dropna(axis=0, how='any', inplace=True)
    print('df shape (after dropnan):', df.shape)


    df_lst_2 = []
    for label in ('tire', 'construct', 'rain', 'deer'):
        df_lst_2.append(window_calculate(df, label, window_size))

    # concatnate & return
    df_wind = pd.concat(df_lst_2, axis=0)
    print('df_wind.shape', df_wind.shape)
    return df_wind

def combined_dataloader(features: List, window_size=30) -> pd.DataFrame:
    eyetrk_list = []
    daq_list = []
    for p_id in range(1, 33):
        # no data from those Participants
        if p_id in {3, 20, 25, 32}: continue
        # Read eye-trking data
        df_eyetrk_file = '../P%d/P%d-eyetrk_wind_label.txt'%(p_id, p_id)
        df_eyetrk = pd.read_csv(df_eyetrk_file, sep='\t')
        eyetrk_list.append(df_eyetrk)
        # Read daq data
        daq_file = '../P%d/P%d-merged_v2.txt'%(p_id, p_id)
        df_daq = pd.read_csv(daq_file, sep='\t')
        daq_list.append(df_daq)

    # concatnate daq data 
    bigDF_eyetrk = pd.concat(eyetrk_list, axis=0)
    bigDF_eyetrk.drop(columns=['Label'], axis=1, inplace=True)
    bigDF_daq = pd.concat(daq_list, axis=0)
    if bigDF_eyetrk.shape[0] != bigDF_daq.shape[0]:
        raise Exception('daq and eyetrk DataFramse must have same number of rows')
    big_df = pd.concat([bigDF_daq, bigDF_eyetrk], axis=1)
    big_df = big_df[features]

    # check NaN values and drop
    print('big_df shape (before dropnan):', big_df.shape)
    print('total nan:', big_df.isna().sum().sum())
    big_df.dropna(axis=0, how='any', inplace=True)
    print('df shape (after dropnan):', big_df.shape)


    df_lst_2 = []
    for label in ('tire', 'construct', 'rain', 'deer'):
        df_lst_2.append(window_calculate(big_df, label, window_size))

    # concatnate & return
    df_wind = pd.concat(df_lst_2, axis=0)
    print('df_wind.shape', df_wind.shape)
    
    return df_wind


#%%
#============================================
#                TESTING
#============================================
# daq_features = [
#         'VDS_Brake_Pedal_Force0',
#         'VDS_Veh_Speed0',
#         'VDS_Steering_Wheel_Angle0',
#         'VDS_Steering_Wheel_Angle_Rate0',
#         'SCC_Lane_Deviation1'   # offset from center of lane
#         ]
# df = daq_dataloader(['Label']+daq_features)
# print(df.shape)


# eyetrk_features = [
#         'Lft X Pos',
#         'Lft Y Pos',
#         'Lft Pupil Diameter',
#         'Rt X Pos',
#         'Rt Y Pos',
#         'Rt Pupil Diameter',
#         'L Eyelid Opening',
#         'R Eyelid Opening'
#         ]
# df = raw_eyetrk_dataloader(['Label']+features)
# print(df.shape)

# df = combined_dataloader(['Label'] + daq_features + eyetrk_features)
# print('df.shape', df.shape)
