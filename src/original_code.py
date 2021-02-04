""" helper library for routine functions """
import glob
import os
import skimage
import numpy as np
from skimage.color import gray2rgb
from tensorflow.keras.applications.vgg16 import preprocess_input
import warnings
import itertools
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from skimage.transform import resize
from scipy.spatial.distance import cdist




def kmeans(X, n_clusters=6, n_iter=100):
    # start n_clusters random data points as cluster centers 
    init_idx = np.random.choice(X.shape[0], size=n_clusters) 
    centers = X[init_idx]
    for t in range(n_iter):
        # compute cluster membership
        # cdist computes the distance between each pair of points
        # between the two input arrays
        labels = np.argmin(cdist(X, centers), axis=1)
    
        # update each cluster center to centroid of cluster members
        for label in range(n_clusters):
            indicator = (labels == label)
            centers[label] = np.sum(X[indicator], axis=0) / np.sum(indicator)
    return labels

