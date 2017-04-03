#-*- coding:utf-8 -*-

import matplotlib.image as mp_image
filename = 'packt.jpeg'

input_image = mp_image.imread(filename)

# print('input dim = {}'.format(input_image.ndim))
# print('input shape = {}'.format(input_image.shape))
#
# import matplotlib.pyplot as plt
# plt.imshow(input_image)
# plt.show()

import tensorflow as tf
# my_image = tf.placeholder("unit8", [None, None, 3])
my_image = tf.placeholder('unit8', [None, None, 3])
