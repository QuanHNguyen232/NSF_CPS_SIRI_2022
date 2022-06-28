from numpy import void
import pandas as pd
from argparse import ArgumentParser

def accum_csv(out_name: str) -> void:
    feat_list = None
    with open('./feat_list.txt', 'r') as f:
        # Read all features
        feat_list = f.readline().replace('\n', '').split(',')
        # Read all csv files
        df_list = [pd.read_csv(feat, header=None, prefix=feat.replace('.csv', '_')) for feat in feat_list]
        # Concatnate all df into 1 df
        df = pd.concat(df_list, axis=1)
        # Save df as csv file
        df.to_csv(out_name)
        
        print('done concat and create {%s} csv'%(out_name))

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(dest='output_name', help='output file name', metavar='.csv')
    args = parser.parse_args()

    accum_csv(args.output_name)
    