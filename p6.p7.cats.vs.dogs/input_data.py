# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:17:49 2018

@author: Gavin.Huang
"""

#import tensorflow as tf
import numpy as np
import os


# image size
image_width = 208
image_height = 208

ROOT_DIR = 'C:/Users/gavin.huang/Documents/udacity-lessons/p6.p7.cats.vs.dogs'
TRAIN_DIR = ROOT_DIR + '/data/train/'
TEST_DIR = ROOT_DIR + '/data/test/'

#print(TRAIN_DIR)
#print(TEST_DIR)

def get_files(file_dir):
    cats = []
    label_cats = []
    dogs = []
    label_dogs = []
    for file in os.listdir(file_dir):
        name = file.split(sep='.')
        if name[0] == 'cat':
            cats.append(file_dir + file)
            label_cats.append(0)
        elif name[0] == 'dog':
            dogs.append(file_dir + file)
            label_dogs.append(1)
        else:
            print('Invalid data: ' + file)
    print('There are %d cats\nThere are %d dogs' %(len(cats), len(dogs)))
    
    image_list = np.hstack((cats, dogs))
    label_list = np.hstack((label_cats, label_dogs))
    
    temp = np.array([image_list, label_list])
    temp = temp.transpose()
    np.random.shuffle(temp)
    
    image_list = list(temp[:, 0])
    label_list = list(temp[:, 1])
    label_list = [int(i) for i in label_list]
    
    return image_list, label_list
    




