import pandas as pd
import random
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras import layers
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model


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


def build_model(training, testing):
    tokenizer = Tokenizer(num_words=500)
    tokenizer.fit_on_texts(training['training_features'])

    X_train = tokenizer.texts_to_sequences(training['training_features'])

    vocab_size = len(tokenizer.word_index) + 1

    maxlen = 150

    X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)

    encoder = LabelEncoder()
    y_train = encoder.fit_transform(training['training_target'])

    embedding_dim = 50

    model = Sequential()
    model.add(layers.Embedding(input_dim=vocab_size,
                               output_dim=embedding_dim,
                               input_length=maxlen))
    model.add(layers.GlobalAveragePooling1D())
    model.add(layers.Dense(10, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    model.fit(X_train, y_train,
                          epochs=50, verbose=True,
                          batch_size=10)
    model.summary()
    return model


if __name__ == "__main__":
    input_file = "Sprint #1 Data Gathering - Sheet1.csv"

    training, testing = parse(input_file)
    model = build_model(training, testing)
    model.save('predictor.h5', True, True)
    
    #TO LOAD MODEL model = load_model('predictor.h5')
    
    #To predict 
    tokenizer = Tokenizer(num_words=500)
    tokenizer.fit_on_texts("surprise")
    input = tokenizer.texts_to_sequences("surprise")
    input = pad_sequences(input, padding='post', maxlen=50)
    prediction = model.predict(input)
    print(prediction)
    
