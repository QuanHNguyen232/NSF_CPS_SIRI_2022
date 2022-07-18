# %%
import pandas as pd

# %%
def modify_miniSim(p_id):

    file_id = 'P%d'%(p_id)
    folder = file_id + '/Eye Tracking/'

    file_1 = file_id + '.miniSim'
    outname = file_id +'-miniSim-modified.txt'

    start = 4
    end = start + 10

    headers_name = ['Frames0', 'X', 'System Time']

    # read .miniSim file
    df_sim = pd.read_csv(folder + file_1, header=None, names=headers_name, dtype=str)
    # change eye-tracking col
    df_sim['System Time'] = df_sim['System Time'].apply(lambda x : str(x).replace('.', '')[start:end])

    # Save df as file
    if df_sim.isna().sum().sum() == 0:
        df_sim.to_csv(folder + outname, header=True, index=False, sep='\t', mode='a')
    else:
        print('########### MISSING VALUES ###########')
        return False
    
    print('modify_miniSim func -- create {%s} -- DONE'%(outname))
    return True

# %%
if __name__ == '__main__':

    for i in range(1, 33):
        
        print('=== ID ==== P%d ==='%(i))
        if not modify_miniSim(i):
            break

    print('convert-miniSim-txt.py -- DONE')
