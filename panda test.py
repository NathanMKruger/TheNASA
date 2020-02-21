import pandas as pd
import random

def main():
    df = pd.read_csv('Sprint #1 Data Gathering - Sheet1.csv')
    print(df)

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

#    return [testing_data, training_data]
