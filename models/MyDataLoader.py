#%%
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from typing import List
plt.style.use('seaborn')

#%% DATALOADER
def daq_dataloader(features: List, window_size=30) -> pd.DataFrame:
    df_lst = []
    for p_id in range(1, 33):
        if p_id == 9: continue
        filename = '../P%d/P%d-merged_v2.txt'%(p_id, p_id)
        df_person = pd.read_csv(filename, sep='\t')
        df_lst.append(df_person)

    df = pd.concat(df_lst, axis=0)
    print('df shape:', df.shape)
    print('total nan:', df.isna().sum().sum())
    
    df = df[features]

    # windowing and calculate min/max/mean/etc.
    df_tire = df[df['Label']=='tire']
    df_construct = df[df['Label']=='construct']
    df_rain = df[df['Label']=='rain']
    df_deer = df[df['Label']=='deer']
    methods = ['max', 'min', 'mean', 'median', 'std']
    df_tire = df_tire.groupby(np.arange(len(df_tire.index)) // window_size)[df_tire.columns].agg(methods)
    df_construct = df_construct.groupby(np.arange(len(df_construct.index)) // window_size)[df_construct.columns].agg(methods)
    df_rain = df_rain.groupby(np.arange(len(df_rain.index)) // window_size)[df_rain.columns].agg(methods)
    df_deer = df_deer.groupby(np.arange(len(df_deer.index)) // window_size)[df_deer.columns].agg(methods)

    # add label
    df_tire['Label'] = 'tire'
    df_construct['Label'] = 'construct'
    df_rain['Label'] = 'rain'
    df_deer['Label'] = 'deer'

    # concatnate
    df_types = [df_tire, df_construct, df_rain, df_deer]
    df_wind = pd.concat(df_types, axis=0)
    print('df_wind.shape', df_wind.shape)
    return df_wind

#%%
# plt.plot(df_tire['VDS_Veh_Speed0']['mean'], label='df_tire')
# plt.plot(df_construct['VDS_Veh_Speed0']['mean'], label='df_construct')
# plt.plot(df_rain['VDS_Veh_Speed0']['mean'], label='df_rain')
# plt.plot(df_deer['VDS_Veh_Speed0']['mean'], label='df_deer')
# plt.legend()
# plt.show()
#%%

# #%%
# y = df['Label']
# le = LabelEncoder()
# le.fit(y)
# classes = le.classes_
# y_enc = le.transform(y)
# df['Label'] = le.transform(y)
# print(classes)

#%% PLOTTING

# for method in methods:
#     plt.plot(df_wind['VDS_Veh_Speed0'][method], label=method)
#     plt.legend()
#     plt.show()

