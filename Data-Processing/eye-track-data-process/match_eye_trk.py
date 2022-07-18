#%%
import pandas as pd
import math
from typing import List

#%%

def calc_loss(time_true, time_pred) -> float:
  val = math.sqrt( (time_true-time_pred)**2 + (time_true-time_pred)**2 )
  return val

def get_timeLst(p_id):
    
    window_name = './P%d/P%d-merged_v2.txt'%(p_id, p_id)
    df_window = pd.read_csv(window_name, sep='\t')

    times = []

    for _, row in df_window.iterrows():
      times.append(row['System Time'])

    print('get_timeLst func --- DONE')
    return times
    
# TEST
# time_ls = get_timeLst(2)
# print(len(time_ls))


def time_matching(miniSim_time, window_time: List) -> int:
  min_loss = math.pow(2, 30)
  ret_time = 0
  # iterate through window to find matched time
  for time in window_time:
    loss = calc_loss(miniSim_time, time)
    
    if loss < min_loss:
      min_loss = loss
      ret_time = time
  if ret_time==0: print('cant find miniSim_time', miniSim_time)
  return ret_time


def get_match_vals(p_id):
  eyetrk_name = './P%d/Eye Tracking/P%d-modified.txt'%(p_id, p_id)
  df_eyetrk = pd.read_csv(eyetrk_name, sep='\t')
  
  merge_name = './P%d/P%d-merged_v2.txt'%(p_id, p_id)
  df_meregd = pd.read_csv(merge_name, sep='\t')
  lst_time = df_meregd['System Time'].to_list()

  idx_time_lst = []
  curr_idx = 0
  for idx, miniSim_time in enumerate(lst_time):
    # print('curr_idx', curr_idx)
    time_match = time_matching(miniSim_time, df_eyetrk['System Time'].to_list())
    # print('miniSim_time', miniSim_time, 'time_match', time_match)
    idx_match = df_eyetrk[df_eyetrk['System Time'] == time_match].index.to_list()[0]
    # print('idx_match', idx_match)
    idx_time_lst.append((idx_match, time_match))
    # curr_idx = idx_match+1 if (idx % 300 != 0) else 0


    if idx%100==0:
      print('p_id', p_id, 'idx', idx, '\t idx_match', idx_match, '\t match', miniSim_time,'->',time_match)
  return idx_time_lst




def get_window_eyetrk(p_id, idx_lst):
  eyetrk_name = './P%d/Eye Tracking/P%d-modified.txt'%(p_id, p_id)
  df_eyetrk = pd.read_csv(eyetrk_name, sep='\t')
  out_name = './P%d/P%d-eyetrk_wind.txt'%(p_id, p_id)

  df = pd.DataFrame(columns=['eyetrk_idx'] + df_eyetrk.columns.to_list())

  for idx in idx_lst:
    row = df_eyetrk.iloc[idx]
    df.loc[len(df.index)] = [idx] + row.to_list()

  #  check missing
  total_nan = df.isna().sum().sum()
  print('total_nan', total_nan)
  print('df shape', df.shape)

  # Save to file
  if total_nan == 0 and df.shape[0]==1200:
      df.to_csv(out_name, header=True, index=False, sep='\t', mode='a')
      print('Saved -- %s'%out_name)
  else:
      print('#########################')
      print(f'total_nan: {total_nan} --- df.shape: {df.shape}')
      print('#########################')
      return False, df
  
  print('get_window_eyetrk func --- DONE')
  return True, df

#%%
# TEST

p_id = 9

ls = get_match_vals(p_id)
print(len(ls))

idx_lst = [i[0] for i in ls]
isDone, df = get_window_eyetrk(p_id, idx_lst)

print(idx_lst[:10])


