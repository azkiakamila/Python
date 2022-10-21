# -*- coding: utf-8 -*-
"""UTS2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CdxXWJvRdwXEiN7L69ZlRzBib9OdmiFn
"""

#Azkia Kamila ; 21091397027 ; 2021A
#UTS2

#multiple perceptron/neuron batch and multiple layer

#inisialisasi numpy
import numpy as np

#inisialisasi variabel (input 10 ; batch 6 = matrix 6*10)
inputs = [[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 1.5],
          [3.0, 5.0, 5.1, 4.6, 6.5, 7.0, 9.9, 1.7, 7.9, 3.0],
          [0.1, 0.3, 5.0, 6.1, 7.8, 5.1, 9.8, 4.3, 5.0, 3.2],
          [0.3, 5.3, 9.0, 6.3, 7.8, 5.5, 6.1, 3.7, 9.2, 6.8],
          [2.0, 9.6, 4.2, 2.9, 5.3, 6.4, 5.0, 6.9, 0.7, 0.5],
          [0.2, 5.1, 4.3, 4.9, 9.6, 7.0, 6.0, 8.6, 4.3, 1.9]]

#panjang weights = panjang inputs(10) ; jumlah weights = jumlah neuron(5)
weights1 = [[-0.25, 2.5, 5.3, 9.2, -6.1, 8.0, 1.5, 7.3, 9.9, 5.1],
           [-0.5, 5.6, 7.8, 3.2, 9.1, 6.4, -7.3, 0.5, 1.9, 2.7],
           [9.5, -0.3, 0.65, -7.3, 5.1, 2.0, 7.0, -6.0, 5.0, 4.0],
           [-0.2, 4.1, 5.0, 3.0, 1.0, -8.6, 2.8, -9.0, 4.1, 0.35],
           [-0.05, 1.0, 3.0, -8.1, 6.4, 9.0, 7.3, 4.5, 6.2, -0.32]]

#jumlah biases pada layer1 adalah 5 neuron
biases1 = [9.0, 0.3, 0.2, 1.5, 8.4]

#panjang weights = neuron layer1(5) ; jumlah weights = jumlah neuron layer2(3)
weights2 = [[0.3, 5.3, 9.0, 6.3, 7.8],
            [2.0, 9.6, 5.3, 6.4, 0.5],
            [9.6, 7.0, 6.0, 8.6, 1.9]]

#jumlah biases pada layer2 adalah 3 neuron
biases2 = [-1, 2,-0.5]

#command untuk menghitung layer1 menggunakan inputs, weights1, dan biases1
layer1_outputs = np.dot(inputs, np.array(weights1).T) + biases1

#command untuk menghitung layer2 menggunakan hasil perhitungan pada layer1
layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2

#print output layer2
print(layer2_outputs)