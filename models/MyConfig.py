MY_SEED = 13

daq_features = [
    'VDS_Brake_Pedal_Force0',
    'VDS_Veh_Speed0',
    'VDS_Steering_Wheel_Angle0',
    'VDS_Steering_Wheel_Angle_Rate0',
    'SCC_Lane_Deviation1'   # offset from center of lane
    ]

eyetrk_features = [
    'Lft X Pos',
    'Lft Y Pos',
    'Lft Pupil Diameter',
    # 'L Eyelid Opening', # useless
    'Rt X Pos',
    'Rt Y Pos',
    'Rt Pupil Diameter',
    # 'R Eyelid Opening'  # useless
    ]

default_daq_feats_drop = [
    'old_idx_x',
    'Frames0',
    'X',
    'System Time',
    'old_idx_y',
    '_merge'
]

default_eyetrk_feats_drop = [
    'eyetrk_idx',
    'Obsv.',
    'Frame',
    'Capture Time',
    'System Time',
    'Sensor Time'
]