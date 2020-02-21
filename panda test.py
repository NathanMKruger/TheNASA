import random

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder


def parse(name):
    df = pd.read_csv(name)
    #print(df)
    df2 = pd.DataFrame(df).drop(columns='Site')
    print("Raw Data")
    print('=====')
    print(df2)
    #print(df)
    indices = random.sample(range(1, df2.index.stop - 1), 3)
    indices.sort()
    #print(indices)
    #using 'A','B' as temporary names for easier manipulation
    testing_data = pd.DataFrame(columns = ['A', 'B'])
    for i in range(0, 3):
        testing_data = testing_data.append({'A' : df2.iat[indices[i], 0], 'B' : df2.iat[indices[i], 1]}, ignore_index = True)
    testing_data.columns = ['testing_features', 'testing_target']
    print('=====')
    print("Printing Testing Data...")
    print('=====')
    print(testing_data)
    #testing data created
    print('=====')
    print('Testing Data Created. Creating Training Data...')
    print('=====')
    indices.sort(reverse=True)
    training_data = pd.DataFrame(df2)
    training_data.columns = ['A', 'B']
    for i in range(0,3):
        training_data = training_data.drop(training_data.index[indices[i]])
    training_data = training_data.reset_index(drop=True)
    training_data.columns = ['training_features', 'training_target']
    print(training_data)

    return training_data, testing_data


def data_cleaning(training_data, testing_data):
    training_values = np.array(training_data)
    testing_values = np.array(testing_data)
    label_encoder = LabelEncoder()
    training_encoded = label_encoder.fit_transform(training_values)
    testing_encoded = label_encoder.fit_transform(testing_values)
    return training_encoded, testing_encoded


def build_model(training_features, training_target):
    model = tf.keras.Sequential([keras.layers.Dense(units=training_features.shape[1], activation='relu',
                                                    input_shape=[training_features.shape[1]]),
                                 keras.layers.Dense(units=64, activation='relu'),
                                 keras.layers.Dense(units=64, activation='relu'),
                                 keras.layers.Dense(units=1, activation='softmax')])

    model.compile(optimizer="SDG", loss='mean_squared_error', metrics=['accuracy'])

    model.fit(training_features, training_target.values, epochs=50)

    return model


if __name__ == "__main__":
    input_file = "Sprint #1 Data Gathering - Sheet1.csv"

    training, testing = parse(input_file)
    training, testing = data_cleaning(training, testing)

    model = build_model(training['training_features'], training['training_target'])
    output = model.predict(testing['testing_features'])

    print('+++++TESTING+++++')
    print(testing)
    print('+++++++++++++++++\n')
    print('+++++PREDICTED++++++')
    print(output)
    print('+++++++++++++++++\n')
