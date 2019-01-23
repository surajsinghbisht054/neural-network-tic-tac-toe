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


import csv

# function to rearrange dataset
def arrange_dataset(dataset):
    # iterate dataset
    for row in dataset:
        # input
        inp = row[-1]

        for cell in row[0:]:
            out = cell
            dset = [inp, out]
            inp = out[:]
            yield dset



class DatasetCollecter:
    def __init__(self, filepath='dataset.csv.tmp'):
        self.filepath = filepath
        self.file = open(self.filepath, 'w')
        self.key = []
        self.value = []
        self.invoke = 0
        
    def save(self):
        # csv writer
        writer = csv.writer(self.file, quoting=csv.QUOTE_MINIMAL)
        for a in zip(self.key, self.value):
            writer.writerow(a)
        return
        
    def close(self):
        self.save()
        self.file.flush()
        self.file.close()
        return
    
    def __str__(self):
        return '<DatasetCollecter|Item:{}|Tries:{}>'.format(len(self.key), self.invoke)
    def __repr__(self):
        return "<DatasetCollector:{}>".format(len(self.key))
    
    
    def __setitem__(self, key, value):
        if key not in self.key:
            self.key.append(key)
            self.value.append(value)
        self.invoke += 1
        return
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        return self.close()
    



# Trigger
if __name__=='__main__':
    print "Welcome!"


