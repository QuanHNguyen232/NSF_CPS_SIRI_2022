from numpy import void
import pandas as pd
from argparse import ArgumentParser

def accum_csv(out_name: str, data_extension = '.txt') -> None:
    """
    Merge each feature data file into a big dataset since each feature is exported as a seperate file from convert_daq_txt.m (Matlab)
    
    Arguments:
    out_name -- file name of output file (expect .txt file)
    data_extension -- OPTIONAL: file extension of those feature data file (expect: .txt as results from convert_daq_txt.m)
    
    Returns:
    None -- create a merged dataset named 'out_name'
    """
    with open('./feat_list.txt', 'r') as f:
        # Read all features
        feat_list = f.readline().replace('\n', '').split(',')
        # Read all csv files
        df_list = [pd.read_csv(feat + data_extension, header=None, prefix=feat.replace('.csv', '_')) for feat in feat_list]
        # Concatnate all df into 1 df
        df = pd.concat(df_list, axis=1)
        # Save df as file
        df.to_csv(out_name, header=True, index=False, sep='\t', mode='a')
        
        print('accum_csv func -- concat and create {%s} -- DONE'%(out_name))

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(dest='output_name', help='output file name', metavar='.txt')
    parser.add_argument('-x', '--extension', help='data files extension')
    args = parser.parse_args()

    if args.extension:
        accum_csv(args.output_name, args.extension)
    else:
        accum_csv(args.output_name)
        
    print('accum_csv.py -- DONE')
    
    # terminal: 
    #       py accum_csv.py filename.txt
    # or    py accum_csv.py filename.txt -x extension
    # with:
    #   extension: csv or txt by default
