import pandas as pd
import numpy as np

file_id = 'P2'
folder = file_id + '/Eye Tracking/'

file_1 = file_id + '.miniSim'
outname = file_id +'-miniSim(modified).txt'

start = 4
end = start + 9

headers_name = ['Frames0', '?_time', 'merge']

# read .miniSim file
df_sim = pd.read_csv(folder + file_1, header=None, names=headers_name, dtype=str)
# change eye-tracking col
df_sim['merge'] = df_sim['merge'].apply(lambda x : str(x).replace('.', '')[start:end])

# Save df as file
df_sim.to_csv(folder + outname, header=True, index=False, sep='\t', mode='a')

print(df_sim.head(5))
print(df_sim.shape)