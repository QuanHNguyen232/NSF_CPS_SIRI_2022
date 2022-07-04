import pandas as pd
import numpy as np


file_1 = 'P13.miniSim'
outname = 'P13-miniSim.txt'
headers_name = ['Frames0', '?_time', 'eye-track_time']

# read .miniSim file
df_sim = pd.read_csv(file_1, header=None, names=headers_name, dtype=str)
# Save df as file
df_sim.to_csv(outname, header=True, index=False, sep='\t', mode='a')

print('miniSim-to-txt.py -- DONE')