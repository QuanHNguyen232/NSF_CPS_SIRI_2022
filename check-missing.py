import pandas as pd

def check_missing(filename: str):
    try:
        df = pd.read_csv(filename, sep='\t')
        
        x=7 # 28 feats
        print(df.isna().sum()[:x*1], '\n')
        print(df.isna().sum()[x*1:x*2], '\n')
        print(df.isna().sum()[x*2:x*3], '\n')
        print(df.isna().sum()[x*3:x*4], '\n')
        total_nan = df.isna().sum().sum()
        print('total NaN:', total_nan, '\n')
        total_null = df.isnull().sum().sum()
        print('total NULL:', total_null, '\n')
        print('shape:', df.shape, '\n')
        print('DF-TAIL',df.tail(5), df.shape, '\n')
        
        print('check_missing func -- file {%s} -- DONE'%(filename))

        result = True
        if total_nan > 0 and total_null > 0:
            print('NAN or NULL values -- file {%s}'%filename)
            print('Nan INDICES', df[df.isna().any(axis=1)].index)
            print('NULL INDICES', df[df.isnull().any(axis=1)].index)
            result = False
        if df.shape[0]<100000:
            print('NOT ENOUGH DATA -- file {%s}'%filename)
            result = False
        return result
    except:
        print('check_missing func -- ERR')
        return False




if __name__ == '__main__':
    for i in range(29, 33):
        idx = i
        filename = 'P%d/Eye Tracking/P%d(modified).txt'%(idx, idx)
        if not check_missing(filename):
            print('ERR -- ID-', i)
            break
    

    print('check-missing.py -- DONE')