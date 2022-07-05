import pandas as pd
import numpy as np
from argparse import ArgumentParser


def merge_daq_miniSim(out_name: str, file_1: str, file_2: str, merge_on: str) -> pd.DataFrame:
    """
    Merge dataset file (expect: .txt) with .miniSim file
    Merge LEFT based on file_1
    
    Arguments:
    out_name -- file name of output file (expect .txt file)
    file_1 -- file name of main file wanted to be added (expect .txt file)
    file_2 -- file name want to add data to file_1 (expect .txt file)
    merge_on -- column name to merge (must exist on both file_1 and file_2)

    Returns:
    None -- create a merged named 'out_name'
    """

    df_daq = pd.read_csv(file_1, sep='\t', dtype=str)
    df_sim = pd.read_csv(file_2, sep='\t', dtype=str)

    print(df_sim.shape, df_daq.shape)

    df = pd.merge(df_daq, df_sim, how='right', on=merge_on, indicator=True)
    print(df.shape)

    df.to_csv(out_name, header=True, index=False, sep='\t', mode='a')
    print('merge_daq_miniSim func -- create {%s} -- DONE'%(out_name))

    return df

def test_merging(df: pd.DataFrame) -> None:
    err = df[df['_merge']!='both']
    print('err', err)
    # .miniSim miss frame 43284 and 149199 (P13 data)

    err1 = df[df['_merge'].isna()]
    print('err1', err1)
    err2 = df[df['_merge'].isnull()]
    print('err2', err2)
    # Everything else are good (P13 data)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(dest='output_name', help='output file name', metavar='.txt')
    parser.add_argument(dest='file_1', help='file want to merge', metavar='.txt')
    parser.add_argument(dest='file_2', help='file want to merge 2', metavar='.txt')
    parser.add_argument(dest='merge_on', help='column used to merge', metavar='.txt')
    args = parser.parse_args()

    merge_daq_miniSim(args.output_name, args.file_1, args.file_2, args.merge_on)
    
    print('read-miniSim.py -- DONE')
    
    # terminal: 
    # py read-miniSim.py out_name file_1 file_2 merge_on
    # with:
    #     file_1 = 'accum-data.txt'
    #     file_2 = 'P13-miniSim.txt'
    #     merge_on = 'Frames0'
    
