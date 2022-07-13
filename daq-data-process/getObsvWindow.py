# %%
import pandas as pd

# %%
A, B, C, D = 'tire', 'construct', 'rain', 'deer'
treatment_lists = [
    [A, B, D, C],
    [B, C, A, D],
    [C, D, B, A],
    [D, A, C, B]
    ]
P_frames_list = [
    [50826, 65919, 121436, 97858],  # P1
    [89858, 36914, 55840, 114092],
    [134243, 109559, 56300, 73323],
    [76470, 123476, 103871, 55829],
    [43099, 59643, 120083, 93433],  # P5
    [111764, 64282, 79901, 135054],
    [137660, 113884, 61526, 79533],
    [88528, 134399, 114169, 66391],
    [63959, 79937, 133677, 110461],
    [120405, 66692, 83382, 145334], # P10
    [143883, 119661, 68025, 84075],
    [84549, 128888, 109516, 63726],
    [71785, 89432, 149195, 122859],
    [118121, 67393, 84450, 141595],
    [139995, 117030, 68326, 84095], # P15
    [97091, 142001, 122148, 75767],
    [43128, 60117, 115427, 90974],
    [88988, 42088, 57144, 112252],
    [140332, 118307, 69124, 86216],
    [57247, 104418, 84740, 32877],  # P20
    [67630, 84789, 143394, 118003],
    [125148, 78349, 93557, 146851],
    [139736, 115887, 66145, 83813],
    [89435, 133931, 114855, 68730],
    [45443, 64558, 122321, 97022],  # P25
    [78947, 28233, 45849, 103336],
    [122099, 99538, 49027, 68150],
    [108200, 159568, 136320, 78933],
    [64624, 83664, 144745, 117541],
    [133970, 74728, 100974, 158401],    # P30
    [141100, 116812, 66234, 84601],
    [87512, 130879, 111664, 67772]
    ]


# %%

def get_windows(p_id):
    
    frames_list = P_frames_list[p_id-1]
    df_filename = './P%d/P%d-daq.txt'%(p_id, p_id)
    out_name = './P%d/P%d-obsv_wind.txt'%(p_id, p_id)
    treatment = 4 if p_id%4==0 else p_id%4
    treatment_list = [
        [A, B, D, C],
        [B, C, A, D],
        [C, D, B, A],
        [D, A, C, B]
    ][treatment-1]

    
    df = pd.read_csv(df_filename, sep='\t')
    window_df = pd.DataFrame(columns=['Label', 'old_idx'] + df.columns.to_list())

    for i in range(len(frames_list)):
        # get old idx
        frame = frames_list[i]
        idx = df[df['Frames0'] == frame].index.to_list()[0]
        print('idx: %d --- frame: %d'%(idx, frame))

        # get label
        label = treatment_list[i]
        
        # add rows into window_df
        for j in range(idx - 299, idx + 1):    # get 5s before each obs
            window_df.loc[len(window_df.index)] = [label, j] + df.iloc[j].to_list()

    #  check missing
    total_nan = window_df.isna().sum().sum()
    print('total_nan', total_nan)

    print('window_df shape', window_df.shape)

    # Save to file
    # if window_df.isna().sum().sum() == 0:
    #     window_df.to_csv(out_name, header=True, index=False, sep='\t', mode='a')
    # else:
    #     print('ERR ERR ERR')
    #     return False

    print('get_windows func --- DONE')
    return window_df

# tmp_df = get_windows(2)
# tmp_df
# %%

# Merge w/ miniSim
def get_windows_miniSim(p_id):
    
    frames_list = P_frames_list[p_id-1]
    sys_time_list = []  # for eye-tracking only

    miniSim_name = './P%d/Eye Tracking/P%d-miniSim-modified.txt'%(p_id, p_id)
    df_miniSim = pd.read_csv(miniSim_name, sep='\t')

    window_df = pd.DataFrame(columns=['old_idx'] + df_miniSim.columns.to_list())

    for i in range(len(frames_list)):
        # get old idx
        frame = frames_list[i]
        idx = df_miniSim[df_miniSim['Frames0'] == frame].index.to_list()[0]
        print('idx: %d --- frame: %d'%(idx, frame))

        sys_time_list.append(df_miniSim['System Time'].iloc[idx])

        # add rows into window_df
        for j in range(idx - 299, idx + 1):    # get 5s before each obs
            window_df.loc[len(window_df.index)] = [j] + df_miniSim.iloc[j].to_list()

    #  check missing
    total_nan = window_df.isna().sum().sum()
    print('total_nan', total_nan)
    print('window_df shape', window_df.shape)
    
    # for eye-tracking only
    print('sys_time_list', sys_time_list)

    print('get_windows_miniSim func --- DONE')
    return window_df, sys_time_list

# miniSim_df = get_windows_miniSim(2)
# miniSim_df



# %%

def merge_df(miniSim, daq_df):
    df = miniSim.merge(daq_df, how='left', on='Frames0', indicator=True)
    out_name = './P%d/P%d-merged.txt'%(p_id, p_id)

    #  check missing
    total_nan = df.isna().sum().sum()
    print('total_nan', total_nan)
    print('window_df shape', df.shape)
    
    if total_nan==0:
        df.to_csv(out_name, header=True, index=False, sep='\t', mode='a')
    elif total_nan <= 172:
        df = df.dropna(axis=0)    # check again threshold
        df.to_csv(out_name, header=True, index=False, sep='\t', mode='a')
    else:
        print('====== ERROR ===========')
        return False, None

    print('merge_df func -- DONE')
    return True, df

# %%
for p_id in range(9, 33):

    daq_df = get_windows(p_id)

    miniSim, _ = get_windows_miniSim(p_id)

    isDone, merged_df = merge_df(miniSim, daq_df)

    if not isDone:
        break




# %%

arr = []
for p_id in range(1, 33):
    
    _, sys_time = get_windows_miniSim(p_id)
    arr.append(sys_time)

#%%
for i in arr[30:33]:
    print(i)