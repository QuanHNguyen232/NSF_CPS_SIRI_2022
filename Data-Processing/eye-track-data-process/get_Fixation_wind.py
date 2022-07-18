#%%
import pandas as pd
import math

#%%
p_id = 1
fixation_name = './P%d/Eye Tracking/P%d_Entire_Drive_36mins Fixation-Vergence.txt'%(p_id, p_id)
df_fixation = pd.read_csv(fixation_name, sep='\t')

# df_fixation
#%%

eyetrk_name = './P%d/P%d-eyetrk_wind.txt'%(p_id, p_id)
df_eyetrk = pd.read_csv(eyetrk_name, sep='\t')
print(df_eyetrk.shape)

orig_eyetrk_name = './P%d/Eye Tracking/P%d-modified.txt'%(p_id, p_id)
df_orig_eyetrk = pd.read_csv(orig_eyetrk_name, sep='\t')

# df_eyetrk

#%%
# start_record should be this start time in P1.txt:
# 4734	29098	1204350508499	1635365110705553	1204350348665	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0	0	0	0	0	0	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0	0.000000	0	0.000000
start_record = df_orig_eyetrk['System Time'].iloc[0]    # 5365033882
# change df_orig_eyetrk into "P1\Eye Tracking\P1-miniSim-modified.txt" file

start_1 = df_eyetrk['System Time'].iloc[0]  # 5365575678
end_1 = df_eyetrk['System Time'].iloc[259]

start_2 = df_eyetrk['System Time'].iloc[300]
end_2 = df_eyetrk['System Time'].iloc[559]

start_3 = df_eyetrk['System Time'].iloc[600]
end_3 = df_eyetrk['System Time'].iloc[899]

start_4 = df_eyetrk['System Time'].iloc[900]
end_4 = df_eyetrk['System Time'].iloc[1199]

time_lst = [(start_1, end_1), (start_2, end_2), (start_3, end_3), (start_4, end_4)]

#%%
# real_time_start = 541.727421 / 60  # 9.0288 minutes = 9min 12s
(1635365110705553 - 1635365033882861)/1000000

#%%
print('start', (start_1-5365033882)/1000, '\t end', (end_1-5365033882)/1000, '\t wind_len', (end_1 - start_1)/1000)
print('start', (start_2-5365033882)/1000, '\t end', (end_2-5365033882)/1000, '\t wind_len', (end_2 - start_2)/1000)
print('start', (start_3-5365033882)/1000, '\t end', (end_3-5365033882)/1000, '\t wind_len', (end_3 - start_3)/1000)
print('start', (start_4-5365033882)/1000, '\t end', (end_4-5365033882)/1000, '\t wind_len', (end_4 - start_4)/1000)

#%%

def calc_minLoss(eyetrk_time, fixation_time) -> float:
  return math.sqrt(abs(eyetrk_time-fixation_time))


def find_loc(eyetrk_time):
    min_loss = 9999999999
    min_idx = 0

    for idx, row in df_fixation.iterrows():
        fixation_time = row['Start Time (secs)']

        loss = calc_minLoss(eyetrk_time, fixation_time)
        if loss < min_loss:
            min_loss = loss
            min_idx = idx
    
    return min_idx, min_loss

#%%
time_1 = time_lst[0]

start_time = (time_1[0]-start_record)/1000
end_time = (time_1[1]-start_record)/1000

start_1_idx, start_1_loss = find_loc(start_time)
end_1_idx, end_1_loss = find_loc(end_time)

print('eyetrk time', start_time, end_time)

print(start_1_idx, end_1_idx)

#%%

for fixation_idx in range(start_1_idx, end_1_idx+1):
    fixation_time = df_fixation['Start Time (secs)'].iloc[fixation_idx]
    eyetrk_time = (fixation_time*1000) + start_record
    print(fixation_idx, '->', fixation_time, '\teyetrk_time', eyetrk_time)
