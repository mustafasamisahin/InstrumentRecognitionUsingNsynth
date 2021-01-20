# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def main():
    train_columns = ["note", "pitch", "velocity", 
                        "instrument_source"]
    
    unwanted_columns = ["instrument_source_str", "instrument_family_str", 
                        "instrument_str", "qualities_str", "note_str", "sample_rate", "instrument"]
    
    qualities_columns = ["bright", "dark", "distortion","fast_decay", "long_release", "multiphonic","nonlinear_env", "percussive", "reverb", "tempo-synced"]
    train_columns.extend(qualities_columns)
    train_columns.append('instrument_family')
    
    
    df_train_raw = pd.read_json(path_or_buf='train.json', orient='index')
    df_train = df_train_raw.drop(unwanted_columns, axis=1)
    df_train = df_train.join(pd.DataFrame(df_train.pop('qualities').values.tolist(), index=df_train.index, columns=qualities_columns))
    df_train = df_train[train_columns]

        
    df_test_raw = pd.read_json(path_or_buf='test.json', orient='index')
    df_test = df_test_raw.drop(unwanted_columns, axis=1)
    df_test = df_test.join(pd.DataFrame(df_test.pop('qualities').values.tolist(), index = df_test.index, columns=qualities_columns))
    df_test = df_test[train_columns]
    
    X = df_train[train_columns[:-1]]
        
    y = df_train['instrument_family']
    
    model = KNeighborsClassifier(n_neighbors=13)
        
    model.fit(X,y)
    result_family = model.predict(df_test.loc[:, df_test.columns != 'instrument_family'])
    
    df_testlist = df_test['instrument_family'].values.tolist()
    c = (np.array(df_testlist) == np.array(result_family))
    print('Accuracy: ', np.count_nonzero(c == True) / np.count_nonzero(c == False))

if __name__ == "__main__":
    
    main()