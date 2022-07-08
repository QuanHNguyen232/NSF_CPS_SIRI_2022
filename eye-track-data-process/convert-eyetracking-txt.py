import pandas as pd
import numpy as np

file_id = 'P2'
folder = file_id + '/Eye Tracking/'

file_1 = file_id + '.txt'
outname = file_id + '(modified).txt'

start = 3
end = start + 9

# read .miniSim file
df = pd.read_csv(folder + file_1, sep='\t', dtype=str)
# change eye-tracking col
df['merge'] = df['System Time']
df['merge'] = df['merge'].apply(lambda x : str(x)[start:end])



# Save df as file
df.to_csv(folder + outname, header=True, index=False, sep='\t', mode='a')

print(df.head(5))
print(df.shape)
