#!/usr/bin/python2.7

"""
Rapando Samson
P15/1568/2015
A Python program to do K-Means Clustering 
"""
import kmc

k = kmc.KMC()
k.set_data()
k.get_centroids()
k.get_d(k.centroids)
# print k.centroids
# k.get_d(k.centroids)
