#!/usr/bin/python2.7
"""
Rapando Samson
P15/1568/2015
A Python program to do K-Nearest Neighbors
"""

neighbor = {}
neighbors = []

print "Enter samples : "
names= ['A', 'B', 'C', 'D']
for i in range(4):
    neighbor['name'] = names[i]
    neighbor['acidity'] = int(raw_input("Acidity : "))
    neighbor['weight'] = int(raw_input("Weight : "))
    neighbor['label'] = int(raw_input("Label (0 - Bad, 1 - Good) : "))
    neighbors.append(neighbor)
    neighbor = {}
    print 

sample = {}
sample['acidity'] = int(raw_input("Enter acidity of sample : "))
sample['weight'] = int(raw_input("Enter weight of sample : "))

for i in range(4):
    x = neighbors[i]['acidity'] - sample['acidity']
    y = neighbors[i]['weight'] - sample['weight']

    neighbors[i]['difference'] = pow(x,2) + pow(y,2)

sorted_neighbors = sorted(neighbors, key=lambda k:k['difference'])

total_labels = 0
for i in range(3):
    total_labels += sorted_neighbors[i]['difference']

print

if total_labels > 2:
    print "The sample is Good"
else:
    print "The sample is Bad"