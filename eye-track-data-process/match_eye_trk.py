#%%
import pandas as pd

#%%
miniSim = pd.read_csv('/content/drive/MyDrive/Draft/data/P1-miniSim-modified.txt', sep='\t')
print(miniSim.shape)
eye_trk = pd.read_csv('/content/drive/MyDrive/Draft/data/P1-modified.txt', sep='\t')
print(eye_trk.shape)

eye_trk['System Time'].head(10)


#%%

eye_trk[eye_trk['System Time'] == 5365033951].index

#%%

def minLoss(time_true, time_pred) -> float:
  val = math.sqrt( (time_true-time_pred)**2 + (time_true-time_pred)**2 )
  return val
  
def matching(miniSim_time, sub_window: List) -> int:
  min_loss = 99999999
  ret_val = 0
  for time in sub_window:
    loss = minLoss(miniSim_time, time)
    
    if loss < min_loss:
      min_loss = loss
      ret_val = time

    # print('min_loss %f --- loss: %f --- ret_val: %d'%(min_loss, loss, ret_val))
    
  return eye_trk[eye_trk['System Time'] == ret_val].index, ret_val

#%%
idx, time = matching(5365033930, eye_trk['System Time'].iloc[0:5])
idx[0]

#%%

big_window = eye_trk['System Time'].iloc[9:30].to_list()
big_window

#%%

tmp = [5365034029, 5365034065, 5365034128]  # expect: 1, 7
ret = []
curr_idx = 7
for i in tmp:
  idx, time = matching(i, eye_trk['System Time'].iloc[curr_idx:curr_idx+5])
  print(big_window[curr_idx:curr_idx+5], end='\t')
  print((idx, time))
  if len(idx)>0:
    idx = idx[0]
    ret.append((idx, time))
    curr_idx = eye_trk[eye_trk['System Time'] == time].index[0]+1
ret

#%%

cols = eye_trk.columns.to_list()
tmp_df = pd.DataFrame(columns=['index'] + cols)

for i in range(len(ret)):
  idx = ret[i][0]
  # print(eye_trk.iloc[idx])
  tmp_df.loc[len(tmp_df.index)] = [idx] + eye_trk.iloc[idx].to_list()

for i in range(len(ret)):
  print(tmp_df.iloc[i][4])

tmp_df

