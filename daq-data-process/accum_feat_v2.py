import pandas as pd
from argparse import ArgumentParser

def accum_feat(target_folder:str, out_name:str, data_extension = 'txt') -> None:
    """
    Merge each feature data file into a big dataset since each feature is exported as a seperate file from convert_daq_txt.m (Matlab)
    
    Arguments:
    out_name -- file name of output file (expect .txt file)
    data_extension -- OPTIONAL: file extension of those feature data file (expect: .txt as results from convert_daq_txt.m)
    
    Returns:
    None -- create a merged dataset named 'out_name'
    """

    with open(target_folder + '/feat_list.txt', 'r') as f:
        # Read all features
        feat_list = f.readline().replace('\n', '').split(',')
        # Read all csv files
        df_list = [pd.read_csv(target_folder + '/' + feat + '.' + data_extension, header=None, prefix=feat.replace('.' + data_extension, '')) for feat in feat_list]
        # Concatnate all df into 1 df
        df = pd.concat(df_list, axis=1)
        # check nan
        x=7 # 28 feats
        print(df.isna().sum()[:x*1])
        print(df.isna().sum()[x*1:x*2])
        print(df.isna().sum()[x*2:x*3])
        print(df.isna().sum()[x*3:x*4])
        print(df.isna().sum().sum())
        print(df.tail(5)['Frames0'], df.shape)
        # Save df as file
        if df.isna().sum().sum() == 0:
            df.to_csv(out_name, header=True, index=False, sep='\t', mode='a')
        else:
            print('ERR ERR ERR')
            return False
        
        
    print('accum_feat func -- concat and create {%s} -- DONE'%(out_name))
    return True

if __name__ == '__main__':
    
    num_samples = 1

    for i in range(num_samples):
        daq_id = 'P' + str(i)
        in_folder = './' + daq_id + '/Driving SIM/Each-feat'
        out_file = './' + daq_id + '/' + daq_id + '-daq.txt'
        if not accum_feat(in_folder, out_file):
            break


    print('accum_feat.py -- DONE')
    

    # parser = ArgumentParser()
    # parser.add_argument(dest='output_name', help='output file name', metavar='.txt')
    # parser.add_argument('-x', '--extension', help='data files extension')
    # args = parser.parse_args()

    # if args.extension:
    #     accum_feat(args.output_name, args.extension)
    # else:
    #     accum_feat(args.output_name)

    # terminal: 
    #       py accum_feat.py filename.txt
    # or    py accum_feat.py filename.txt -x extension
    # with:
    #   extension: txt by default or csv
