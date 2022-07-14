
# %%
from typing import List
import pandas as pd
import numpy as np
import os, math, sys
import matplotlib.pyplot as plt
plt.style.use('seaborn')

labels = [('tire', 'b'), ('construct', 'y'), ('rain', 'c'), ('deer', 'r')]
# %%

def calc_minLoss(loc_pred, loc_true) -> float:
  val = math.sqrt(( abs(loc_pred[0])-abs(loc_true[0]) )**2 + ( abs(loc_pred[1])-abs(loc_true[1]) )**2)
  return val

def plt_speed(df: pd.DataFrame, min_idx: List):
    plt.plot(df.speed)
    for i, idx in enumerate(min_idx):
        plt.plot([idx], [df.speed[idx]], labels[i][1]+'o', label=labels[i][0])
    plt.legend()
    plt.xlabel('Time frame')
    plt.ylabel('Speed (mph)')
    plt.show()

def plt_route(df: pd.DataFrame, min_idx: List, obs: List):
    obs_y = [obs[i][0] for i in range(len(obs))]
    obs_x = [obs[i][1] for i in range(len(obs))]
    plt.plot(df.X, df.Y)
    plt.plot(obs_x, obs_y, 'ks', label='obs')
    plt.plot([df.X[0]], df.Y[0], 'g^', label='start')
    for i, idx in enumerate(min_idx):
        plt.plot([df.X[idx]], df.Y[idx], labels[i][1]+'X', label=labels[i][0])
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    plt.show()
# %%
def find_obstacle(p_id):
    print(f'\nP{p_id}')
    folder_path = './P%d/Driving SIM/Each-feat/'%(p_id)
    treatment = 4 if p_id%4==0 else p_id%4

    df = pd.read_csv(folder_path + 'VDS_Chassis_CG_Position.txt', header=None, names=['Y', 'X', 'Z'])
    frames = pd.read_csv(folder_path + 'Frames.txt', header=None, names=['frame'])
    speed = pd.read_csv(folder_path + 'VDS_Veh_Speed.txt', header=None, names=['speed'])
    print(df.shape, frames.shape, speed.shape)

    min_loss = [sys.maxsize]*4
    min_idx = [0]*4

    # left -> right: treatment
    # (Y, X) coordinates
    tire      = [[8882.42, 28219.67],   [3234.04, 12185.81],    [28654.74, 8910.37],    [28235.50, 25054.01]][treatment-1]
    construct = [[21233.69, 26310.47],  [9011.04, 28221.55],    [3157.65, 13339.60],    [23615.03, 10930.66]][treatment-1]
    rain      = [[26676.91, 7426.58],   [21018.29, 26347.51],   [8859.78, 28217.34],    [3309.54, 13891.32]][treatment-1]
    deer      = [[3044.13, 12947.75],   [26651.05, 7403.36],    [21028.52, 26338.19],   [9083.90, 28217.74]][treatment-1]

    obs = [tire, construct, rain, deer]
    for idx, row in df.iterrows():
        Y, X, _ = row
        losses = [calc_minLoss((Y, X), obs[i]) for i in range(len(obs))]

        for i in range(len(obs)):
            if losses[i] < min_loss[i]:
                min_loss[i] = losses[i]
                min_idx[i] = idx

    print(f'idx: {min_idx}')
    print(f'frames:', [frames.frame[i] for i in min_idx])
    print(labels)

    # plot route
    plt_route(df, min_idx, obs)

    # plot speed
    plt_speed(speed, min_idx)

# %%

for i in range(1,5):
    find_obstacle(i)