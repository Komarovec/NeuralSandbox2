import tensorflow as tf
import numpy as np

from statistics import median, mean
from collections import Counter

#AI Framework
from keras.models import Sequential
import keras

class Brain():
    def __init__(self, input_size=3):
        self.learningRate = 1e-3
        self.network = self.neural_network_model(input_size)

    def getResult(self, rawdata):
        data = np.array(rawdata)

        print(data.shape)
        print(data)
        result = self.network.predict(data)

        return result

    def neural_network_model(self, input_size):
        #Create model
        model = keras.Sequential([
            keras.layers.Dense(64, activation=tf.nn.relu, input_dim=1),
            keras.layers.Dense(128, activation=tf.nn.relu),
            keras.layers.Dropout(0.5),
            keras.layers.Dense(4)
        ])

        #Compile model
        model.compile(optimizer='adam', 
                    loss='categorical_crossentropy',
                    metrics=['accuracy'])

        return model

    def fit(self, data):
        X = data[0]
        Y = data[1]

        print(Y)
        print("-----")
        print(X)
        self.network.fit(X, Y, epochs=5, batch_size=32)


        
    """ TFLearn
    def neural_network_model(self, input_size):
        network = input_data(shape=[None,input_size], name='input')

        network = fully_connected(network, 32, activation='relu')
        #network = dropout(network, 0.8)

        network = fully_connected(network, 64, activation='relu')
        #network = dropout(network, 0.8)

        network = fully_connected(network, 32, activation='relu')

        network = fully_connected(network, 4, activation='softmax')
        network = regression(network, optimizer='adam', learning_rate=self.learningRate, loss='categorical_crossentropy', name='targets')

        model = tflearn.DNN(network)

        return model

    def fit(self, data):
        X = data[0]
        Y = data[1]
        self.network.fit({'input': X}, {'targets': Y}, n_epoch=5, show_metric=True, run_id='openai_learning')
    """