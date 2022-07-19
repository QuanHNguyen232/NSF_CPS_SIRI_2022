#
import pandas as pd
import numpy as np
from typing import List

from MyConfig import default_daq_feats_drop, default_eyetrk_feats_drop
#
def window_calculate(df: pd.DataFrame, label:str, window_size:int, methods) -> pd.DataFrame:
    print(df.shape)
    df_label = df[df['Label']==label]
    df_label = df_label.groupby(np.arange(len(df_label.index)) // window_size)[df_label.columns].agg(methods)
    df_label['Label'] = label
    return df_label

# DATALOADER
def daq_dataloader(features:List=None, window_size=30, methods=['mean', 'median', 'std']) -> pd.DataFrame:
    # read data
    filename = '../full-daq-dataset.txt'
    df = pd.read_csv(filename, sep='\t')
    
    # get specific feature
    if features != None:
        features = ['Label'] + features
        df = df[features]
    else:
        df.drop(default_daq_feats_drop, axis=1, inplace=True)
    
    # windowing
    df_lst_2 = []
    for label in ('tire', 'construct', 'rain', 'deer'):
        df_lst_2.append(window_calculate(df, label, window_size, methods))

    # concatnate & return
    df_wind = pd.concat(df_lst_2, axis=0)
    print('df_wind.shape', df_wind.shape)
    return df_wind

def raw_eyetrk_dataloader(features:List=None, window_size=30, methods=['mean', 'median', 'std']) -> pd.DataFrame:
    # read data
    filename = '../full-raw-eyetrk-dataset.txt'
    df = pd.read_csv(filename, sep='\t')
    
    # get specific feature
    if features != None:
        features = ['Label'] + features
        df = df[features]
    else:
        df.drop(default_eyetrk_feats_drop, axis=1, inplace=True)

    # windowing
    df_lst_2 = []
    for label in ('tire', 'construct', 'rain', 'deer'):
        df_lst_2.append(window_calculate(df, label, window_size, methods))

    # concatnate & return
    df_wind = pd.concat(df_lst_2, axis=0)
    print('df_wind.shape', df_wind.shape)
    return df_wind

def combined_dataloader(features:List=None, window_size=30, methods=['mean', 'median', 'std']) -> pd.DataFrame:
    # read data
    filename = '../full-combined-dataset.txt'
    df = pd.read_csv(filename, sep='\t')

    # get specific feature
    if features != None:
        features = ['Label'] + features
        df = df[features]
    else:
        df.drop(list(set(default_daq_feats_drop + default_eyetrk_feats_drop)), axis=1, inplace=True)

    # windowing
    df_lst_2 = []
    for label in ('tire', 'construct', 'rain', 'deer'):
        df_lst_2.append(window_calculate(df, label, window_size, methods))

    # concatnate & return
    df_wind = pd.concat(df_lst_2, axis=0)
    print('df_wind.shape', df_wind.shape)
    
    return df_wind


#
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
# df = daq_dataloader(daq_features)
# print(df.shape)


# eyetrk_features = [
#         'Lft X Pos',
#         'Lft Y Pos',
#         'Lft Pupil Diameter',
#         'Rt Pupil Diameter',
#         'Rt X Pos',
#         'Rt Y Pos',
#         'L Eyelid Opening',
#         'R Eyelid Opening'
#         ]
# df = raw_eyetrk_dataloader(eyetrk_features)
# print(df.shape)

# df = combined_dataloader(daq_features + eyetrk_features)
# print('df.shape', df.shape)
