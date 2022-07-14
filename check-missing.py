#%%
import pandas as pd

#%%
for p_id in range(1, 33):
    if p_id==9: continue
    print('P', p_id)
    filename = './P%d/P%d-merged_v2.txt'%(p_id, p_id)
    df = pd.read_csv(filename, sep='\t')
    
    length = len(df)
    if length != 1200:
        print('MISS LINES')
        break
    # 'tire', 'construct', 'rain', 'deer'
    if len(df[df['Label']=='tire'])!= 300:
        print('MISS tire')
        break
    if len(df[df['Label']=='construct'])!= 300:
        print('MISS construct')
        break
    if len(df[df['Label']=='rain'])!= 300:
        print('MISS rain')
        break
    if len(df[df['Label']=='deer'])!= 300:
        print('MISS deer')
        break
    total_nan = df.isna().sum().sum()
    total_null = df.isnull().sum().sum()
    if total_nan>0 or total_null>0:
        print('NAN/NULL VALUES')
        break
print('success')