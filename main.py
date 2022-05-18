import tensorflow as tf
from tensorflow import keras
from pickle import load
import numpy as np
import pandas as pd


def preprocess_object_features(df):
    arr = object_encoder.transform(df[object_features]).toarray()
    new_df = pd.DataFrame(arr, columns=object_encoder.get_feature_names(), index=df.index)
    df = df.drop(object_features, axis=1)
    df = pd.concat((df, new_df), axis=1)
    return df

def preprocess_numeric_features(df):
    arr = numeric_encoder.transform(df[numeric_features])
    new_df = pd.DataFrame(arr, columns=numeric_features, index=df.index)
    df = df.drop(numeric_features, axis=1)
    df = pd.concat((df, new_df), axis=1)
    return df

def preprocessing_df(df):
    df = preprocess_object_features(df)
    df = preprocess_numeric_features(df)
    return df

def calculate_errors(df):
    df = preprocessing_df(df)
    pred = model.predict(df)
    errors = np.mean((pred - np.array(df))**2, axis=1)
    return errors


if __name__ == '__main__':
    object_features = ['protocol_type', 'service', 'flag']
    numeric_features = ['duration', 'src_bytes', 'dst_bytes', 'land', 
                        'wrong_fragment', 'urgent', 'hot', 'num_failed_logins',
                        'logged_in', 'num_compromised', 'root_shell', 'su_attempted',
                        'num_root', 'num_file_creations', 'num_shells',
                        'num_access_files', 'num_outbound_cmds', 'is_host_login',
                        'is_guest_login', 'count', 'srv_count', 'serror_rate',
                        'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
                        'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate',
                        'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
                        'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
                        'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
                        'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
                        'dst_host_srv_rerror_rate']
    with open('object_encoder.pkl', 'rb') as f:
        object_encoder = load(f)
    with open('numeric_encoder.pkl', 'rb') as f:
        numeric_encoder = load(f)
    model = keras.models.load_model('model.h5')

    path = 'samples.csv'
    df = pd.read_csv(path)
    errors = calculate_errors(df)

    threshold = 0.004
    for error in errors:
        if error > threshold:
            print('bad connection')
        else:
            print('normal.')
