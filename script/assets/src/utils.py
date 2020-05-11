import numpy as np
import tensorflow as tf
#from . import config
from src.config import *


#Function to generate n random messages and keys
def gen_data(n= BATCH_SIZE, msg_len=MSG_LEN, key_len=KEY_LEN):
#def gen_data(n, msg_len, key_len):
    return (np.random.randint(0, 2, size=(n, msg_len))*2-1), \
           (np.random.randint(0, 2, size=(n, key_len))*2-1)


# Xavier Glotrot initialization of weights
def init_weights(name, shape):
    return tf.compat.v1.get_variable(name, shape=shape,
                           #initializer=tf.contrib.layers.xavier_initializer())
                           initializer=tf.initializers.GlorotUniform())