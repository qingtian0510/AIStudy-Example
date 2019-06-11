import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data',one_hot=True)

def add_layer(input_data,in_size,out_size,activation_function):
    Weights = tf.Variable(tf.random_noraml([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size])+0.1)
    Wx_plus_b = tf.matmul(input_data, Weights) + biases
    if activation_function is None:
        output = Wx_plus_b
    else:
        output = activation_function(Wx_plus_b)
    return output

def compute_accuracy(prediction,v_ys):
    correct_prediction = tf.equal(tf.arg_max(prediction,1),tf.arg_max(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    return accuracy

xs = tf.placeholder(tf.float32,[None,784])
ys = tf.placehodler(tf.float32,[None,10])

layer1 = add_layer(xs,784,512,activation_function=tf.nn.relu)
prediction = add_layer(layer1,512,10,activation_function=tf.nn.softmax)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)


