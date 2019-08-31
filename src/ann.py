#!/usr/bin/python
#
# =================================================================
#                       README
# =================================================================
#
#
# Author:
#       Suraj singh bisht
#       surajsinghbisht054@gmail.com
#       www.bitforestinfo.com
#
# -------------------------------------------------------------
#           Please Don't Remove Author Initials
# ------------------------------------------------------------
#
#
# Description:
#           Simple Tic Tac Toe Game Implementation in Python
#
#
#


# import required class
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer, TanhLayer
from pybrain.structure import FullConnection
from pybrain.tools.customxml import NetworkReader, NetworkWriter
from configuration import *
import random
import os
import csv

# OUTPUT PATH
ANN_WEIGHT_BACKUP = '../tmp/computed_weight.weight'


# function to remove unwanted focus from val
def focus(key, val):
    tmp = []
    if True:
            # neutral function
            return (key, val)
    for a, b in zip(key, val):
        if a==b:
            tmp.append(0)
        else:
            tmp.append(b)
    return (key, val)

    
# training dataset
def training_dataset(path):

    # create training dataset class
    dataset = SupervisedDataSet(INPUTNN, OUTPUTNN)

    # read dataset csv file    
    f = open(path, 'r')
    reader = csv.reader(f)

    # iterate rows
    for key, val in reader:
        key, val = eval(key), eval(val)
        key, val = focus(key, val)
        # To make Decision little Unpredectable, Using 1 Random Input Data
        key.append(random.randrange(9)*0.01) # 10 -> To make little impact 

        # we can also use above method to trained our ann in special way, for example:
        # we can use these input as classification of training data.
        # in simple words, when we are passing wining situation, Activate One Input, And Off Other one
        # When, Draw situation taining, turn On another input and close others
        # same with loss situation. maybe, this method can also
        # make this game more interesting.
        dataset.addSample(key, val)
    print "[*] Length of Loaded Samples : {}".format(len(dataset))
    return dataset


# build neural network
def newnetwork():
    # network structure
    net = FeedForwardNetwork()

    # first input layer
    firstlayer = LinearLayer(INPUTNN) # first input layer
    secondlayer = TanhLayer(TANHLYNN) # second tanh layer
    thirdlayer = SigmoidLayer(SIGMODNN) # third sigmod layer
    fourthlayer = LinearLayer(OUTPUTNN) # fourth output layer

    # install network layers into network structure
    net.addInputModule(firstlayer)
    net.addModule(secondlayer)
    net.addModule(thirdlayer)
    net.addOutputModule(fourthlayer)

    # establish connection between layers
    f_s = FullConnection(firstlayer, secondlayer)
    s_t = FullConnection(secondlayer, thirdlayer)
    t_f = FullConnection(thirdlayer, fourthlayer)

    # install connections into network structure
    net.addConnection(f_s)
    net.addConnection(s_t)
    net.addConnection(t_f)

    # install random weight and other process
    net.sortModules()

    return net

def main():
    # check required neural network is new or Old, 
    # if New, Create New One and Then, Start Training
    # if Old, Load Weight And Start Training

    print "[+] Creating Neural Network"
    if os.path.exists(ANN_WEIGHT_BACKUP):
        print "[+] Found, Already Ready To Use Network Weight."
        print "[*] Loading Weight From {}".format(ANN_WEIGHT_BACKUP)
        ann = NetworkReader.readFrom(ANN_WEIGHT_BACKUP)
        
    else:
        # create artificial neural network
        #
        ann = newnetwork()
        print "[*] New Network Created"
    
    # dataset setup
    print "[-] Loading Dataset Data"
    ds = training_dataset('../tmp/generated_dataset.csv')

    print "[*] Loading Complete"
    
    # trainer load
    print "[-] Loading Trainer"
    trainer = BackpropTrainer(ann, ds)

    print "[*] Trainer Ready To Train"

    # trainer ready
    print "[-] Take A Seat, It Will Take Few Minutes To Train...."
    for i in range(50):
        print "[+] Dataset Error Rate : ", trainer.train()
    
    print "[+] Updated Network Saved."
    # save network weight
    NetworkWriter.writeToFile(ann, ANN_WEIGHT_BACKUP)

    return 

# Trigger
if __name__=='__main__':
    main()
