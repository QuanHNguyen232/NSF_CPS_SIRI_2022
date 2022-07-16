#%%
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
plt.style.use('seaborn')

from MyDataLoader import daq_dataloader

#%% CONFIG
MY_SEED = 0
MY_FEATURES = []

#%% CONSTANTS
all_feats = set(pd.read_csv('../P32/Driving SIM/Each-feat/feat_list.txt', sep=',').columns)
remove_cols = [
    'old_idx_x',
    'Frames0',
    'X',
    'System Time',
    'old_idx_y',
    'SCC_Audio_Trigger0',
    'SCC_Collision_Count0',
    'VDS_Chassis_CG_Position0',
    'VDS_Chassis_CG_Position1',
    'VDS_Chassis_CG_Position2',
    'VDS_Chassis_CG_Accel0',
    'VDS_Chassis_CG_Accel1',
    'VDS_Chassis_CG_Accel2',
    'SCC_Eval_Event_SDLP0',
    'SCC_Eval_Event_SDLP1',
    'SCC_Eval_Event_SDLP2',
    'SCC_Eval_Event_SDLP3',
    ]


#%% Load data
features = [
        'Label',
        'VDS_Brake_Pedal_Force0',
        'VDS_Veh_Speed0',
        'VDS_Steering_Wheel_Angle0',
        'VDS_Steering_Wheel_Angle_Rate0',
        'SCC_Lane_Deviation1'   # offset from center of lane
        ]
df = daq_dataloader(features)

df
#%% PREPROCESSING
df.drop(['Label'], axis=1, inplace=True)
std_scaler = StandardScaler()
X_std = std_scaler.fit_transform(df)


#%% KMEANS
distortions = []
max_range = 50
for i in range(1, max_range+1):
    kmeans = KMeans(
        n_clusters=i,
        random_state=MY_SEED
    )
    kmeans.fit(X_std)
    distortions.append(kmeans.inertia_)

# plot
plt.plot(range(1, max_range+1), distortions, marker='o')
plt.show()

#%%
silh_score_ = []
for k in range(2, 20+1):
    kmeans = KMeans(n_clusters=k, random_state=MY_SEED).fit(X_std)
    silh_score = silhouette_score(X_std, kmeans.labels_, metric = 'euclidean')
    silh_score_.append(silh_score)

#%%
plt.plot(silh_score_, 'o-')
plt.xlabel('$k$', fontsize=20)
plt.ylabel('Silhouette Score', fontsize=20)

