# %%
import pandas as pd

# %%
def modify_eye_trk(p_id):
    file_id = 'P%d'%(p_id)
    folder = file_id + '/Eye Tracking/'

    file_1 = file_id + '.txt'
    outname = file_id + '-modified.txt'

    start = 3
    end = start + 10

    # read .miniSim file
    df = pd.read_csv(folder + file_1, sep='\t', dtype=str)
    # change eye-tracking col
    df['System Time'] = df['System Time'].apply(lambda x : str(x)[start:end])



    # Save df as file
    total_nan = df.isna().sum().sum()
    if total_nan == 0:
        df.to_csv(folder + outname, header=True, index=False, sep='\t', mode='a')
    elif total_nan <= len(df.columns):
        df.dropna(axis=0, inplace=True)
        df.to_csv(folder + outname, header=True, index=False, sep='\t', mode='a')
    else:
        print('########### MISSING VALUES ###########')
        return False
        
    print('modify_eye_trk func -- create {%s} -- DONE'%(outname))
    return True

# %%
if __name__ == '__main__':

    for i in range(30, 33):
        
        print('=== ID ==== P%d ==='%(i))
        if not modify_eye_trk(i):
            break
    
    print('convert-eyetracking-txt.py -- DONE')