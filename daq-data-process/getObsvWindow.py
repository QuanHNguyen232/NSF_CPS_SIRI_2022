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
P_idx_list = [
    [28140, 43233, 98750, 75172],   # P1
    [79619, 26675, 45601, 103853],
    [105155, 80471, 27212, 44235],
    [46491, 93497, 73892, 25850],
    [26827, 43371, 103811, 77161],  # P5
    [73234, 25752, 41371, 96524],
    [102102, 78326, 25968, 43975],
    [49063, 94934, 74704, 26926],
    [26194, 42172, 95912, 72696],
    [80697, 26984, 43674, 105626],  # P10
    [103144, 78922, 27286, 43336],
    [47314, 91653, 72281, 26491],
    [28503, 46150, 105913, 79577],
    [75970, 25242, 42299, 99444],
    [98519, 75554, 26850, 42619],   # P15
    [47144, 92054, 72201, 25820],
    [25913, 42902, 98212, 73759],
    [73609, 26709, 41765, 96873],
    [96296, 74271, 25088, 42180],
    [53377, 100548, 80870, 29007],  # P20
    [26450, 43609, 102214, 76823],
    [71218, 24419, 39627, 92921],
    [99903, 76054, 26312, 43980],
    [47858, 92354, 73278, 27153],
    [26117, 45232, 102995, 77696],  # P25
    [76740, 26026, 43642, 101129],
    [99240, 76679, 26168, 45291],
    [56847, 108215, 84967, 27580],
    [26023, 45063, 106144, 78940],
    [85493, 26251, 52497, 109924],  # P30
    [101708, 77420, 26842, 45209],
    [44975, 88342, 69127, 25235]
    ]


# %%

def get_windows(p_id):
    
    idx_list = P_idx_list[p_id-1]
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

    for i in range(len(idx_list)):
        # get old idx
        idx = idx_list[i]
        # get label
        label = treatment_list[i]
        # add rows into window_df
        for j in range(idx - 300, idx + 60):    # get 5s before and 1s after each obs
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
    
    idx_list = P_idx_list[p_id-1]

    miniSim_name = './P%d/Eye Tracking/P%d-miniSim-modified.txt'%(p_id, p_id)
    df_miniSim = pd.read_csv(miniSim_name, sep='\t')

    window_df = pd.DataFrame(columns=['old_idx'] + df_miniSim.columns.to_list())

    for i in range(len(idx_list)):
        # get old idx
        idx = idx_list[i]
        # add rows into window_df
        for j in range(idx - 300, idx + 60):    # get 5s before and 1s after each obs
            window_df.loc[len(window_df.index)] = [j] + df_miniSim.iloc[j].to_list()

    #  check missing
    total_nan = window_df.isna().sum().sum()
    print('total_nan', total_nan)

    print('window_df shape', window_df.shape)
    
    print('get_windows_miniSim func --- DONE')
    return window_df

# tmp_df = get_windows_miniSim(2)
# tmp_df



# %%

def merge_df(miniSim, daq_df):
    df = miniSim.merge(daq_df, how='left', on='Frames0', indicator=True)

    #  check missing
    total_nan = df.isna().sum().sum()
    print('total_nan', total_nan)

    print('window_df shape', df.shape)

    print('merge_df func -- DONE')
    return df

# %%
p_id=1
miniSim, daq_df = get_windows(p_id), get_windows_miniSim(p_id)
merged_df = merge_df(miniSim, daq_df)
merged_df


# %%
nanlist = merged_df.isna().sum().to_list()
print(len(nanlist))
for i in range(len(merged_df.columns)):
    if nanlist[i]>0:
        print(nanlist[i])