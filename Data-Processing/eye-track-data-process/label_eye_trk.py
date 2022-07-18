#%%
import pandas as pd

#%%
for p_id in range(1,33):
    if p_id in {3, 20, 25, 32}: continue    # dont have eye-trk data
    print('P', p_id)
    filename = './P%d/P%d-merged_v2.txt'%(p_id, p_id)
    df = pd.read_csv(filename, sep='\t')

    # df_tire = df[df['Label'] == 'tire']
    # df_construct = df[df['Label'] == 'construct']
    # df_rain = df[df['Label'] == 'rain']
    # df_deer = df[df['Label'] == 'deer']

    # print('len df_tire:', len(df_tire), '\t first-last idx', df['Label'].iloc[0]==df['Label'].iloc[299])
    # print('len df_construct:', len(df_construct), '\t first-last idx', df['Label'].iloc[300]==df['Label'].iloc[599])
    # print('len df_rain:', len(df_rain), '\t first-last idx', df['Label'].iloc[600]==df['Label'].iloc[899])
    # print('len df_deer:', len(df_deer), '\t first-last idx', df['Label'].iloc[900]==df['Label'].iloc[1199])

    eye_trk_name = './P%d/P%d-eyetrk_wind.txt'%(p_id, p_id)
    df_eye_trk = pd.read_csv(eye_trk_name, sep='\t')
    
    # print('first-last Frame', df_eye_trk['Frame'].iloc[0], df_eye_trk['Frame'].iloc[299])
    # print('first-last Frame', df_eye_trk['Frame'].iloc[300], df_eye_trk['Frame'].iloc[599])
    # print('first-last Frame', df_eye_trk['Frame'].iloc[600], df_eye_trk['Frame'].iloc[899])
    # print('first-last Frame', df_eye_trk['Frame'].iloc[900], df_eye_trk['Frame'].iloc[1199])
    
    labels = ['tire', 'construct', 'rain', 'deer']
    label_col = []
    for i in range(len(df_eye_trk)):
        label_col.append(labels[i//300])
    
    # print(label_col[298:302])
    # print(label_col[598:602])
    # print(label_col[898:902])
    
    df_eye_trk.insert(loc=2, column='Label', value=label_col)


    out_name = './P%d/P%d-eyetrk_wind_label.txt'%(p_id, p_id)
    df_eye_trk.to_csv(out_name, header=True, index=False, sep='\t', mode='a')
    print('done')