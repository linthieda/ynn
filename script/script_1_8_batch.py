# required python version: 3.6+

import os
import sys
import src.load_data as load_data
from src import plot_data
from src import layer
from src.network import NeuralNetwork_Dumpable as NN
import src.network as network
import matplotlib.pyplot as plt
import numpy
import os

#  format of data
# disitstrain.txt contains 3000 lines, each line 785 numbers, comma delimited

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
data_filepath = '../data'
data_train_filename = 'digitstrain.txt'
data_valid_filename = 'digitsvalid.txt'
data_test_filename = 'digitstest.txt'

data_train_filepath = os.path.join(path, data_filepath, data_train_filename)
data_valid_filepath = os.path.join(path, data_filepath, data_valid_filename)
data_test_filepath = os.path.join(path, data_filepath, data_test_filename)

print('start initializing...')
network.init_nn(random_seed=1099)

learning_rates = [0.001]
momentums = [0.9]

regularizers = [0.0001]
x_train, y_train = load_data.load_from_path(data_train_filepath)
x_valid, y_valid = load_data.load_from_path(data_valid_filepath)

withBN = True
if not withBN:
    for i2 in range(len(regularizers)):
        for i3 in range(len(momentums)):
            for i4 in range(len(learning_rates)):
                layers = [layer.Linear(784, 100),
                          layer.Sigmoid(100, 100),
                          layer.Linear(100, 25),
                          layer.Sigmoid(25, 25),
                          layer.Linear(25, 10),
                          layer.Softmax(10, 10)]
                name = 'network2' + '-' + str(i2) + '-' + str(i3) + '-' + str(i4) + '.dump'
                myNN = NN(layers, learning_rate=learning_rates[i4], regularizer=regularizers[i2], momentum=momentums[i3])
                myNN.train(x_train, y_train, x_valid, y_valid, epoch=300, batch_size=32)

if withBN:
    for i2 in range(len(regularizers)):
        for i3 in range(len(momentums)):
            for i4 in range(len(learning_rates)):
                layers = [layer.Linear(784, 100),
                          layer.BN(100, 100),
                          layer.Sigmoid(100, 100),
                          layer.Linear(100, 25),
                          layer.BN(25, 25),
                          layer.Sigmoid(25, 25),
                          layer.Linear(25, 10),
                          layer.Softmax(10, 10)]
                name = 'network2' + '-' + str(i2) + '-' + str(i3) + '-' + str(i4) + '.dump'
                myNN = NN(layers, learning_rate=learning_rates[i4], regularizer=regularizers[i2], momentum=momentums[i3])
                myNN.train(x_train, y_train, x_valid, y_valid, epoch=300, batch_size=32)