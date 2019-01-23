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

# import modules
import os
from conditions import p, getaval, win, checkend, pretifyboard
from datasetutils import DatasetCollecter, arrange_dataset
import random
import csv


# create function
os.system('mkdir ../tmp/')
os.system('mkdir ../test/')

# Class To Generate ALl Possible Situations Dataset
class GenerateDataset:
    def __init__(self):

        # generating starting board condition dataset
        self.dataset = self.calculate([0,0,0,0,0,0,0,0,0]) 
        # arranger winning possibilities in starting and draw, loss in end
        self.sorting()
        self.won = []
        self.loss= []
        self.draw= []
        self.filteration()


    # filteration function
    def filteration(self):

        # iterate dataset
        for i in self.dataset:
            # loss
            if win(i[-1], token=-1):
                self.loss.append(i)
            # win
            elif win(i[-1]):
                self.won.append(i)
            # draw
            else:
                self.draw.append(i)

        return


    # our player won
    def selfwin(self):
        return self.won
    
    # our player lose
    def selfloss(self):
        return self.loss

    # gamedraw
    def selfdraw(self):
        return self.draw

    # sorting possibilities
    def sorting(self):
        # perform sorting
        self.dataset = sorted(self.dataset, key=len)
        return

    def __len__(self):
        return len(self.dataset)

    # function to perform calculations
    def calculate(self, bs):

        # main collection list
        tmp = []

        # first turn
        xtmp0=[bs]
    
        print bs
    
        # function to iterate first turn possibilities
        for a in p(bs):
            xtmp1 = xtmp0[:]
            xtmp1.append(a)
            # if game end
            #print xtmp1
            #print checkend(xtmp1)
            if checkend(xtmp1):
                tmp.append(xtmp1)
                continue
        
            # function to iterate second turn possibilities
            for b in p(a, token=-1):
                xtmp2 = xtmp1[:]
                xtmp2.append(b)
                # if game end
                if checkend(xtmp2):
                    tmp.append(xtmp2)
                    continue
        
                # function to iterate third turn possibilities
                for c in p(b):
                    xtmp3 = xtmp2[:]
                    xtmp3.append(c)
                    # check If game end
                    if checkend(xtmp3):
                        tmp.append(xtmp3)
                        continue
        
                    # function to iterate fourth turn possibilities
                    for d in p(c, token=-1):
                        xtmp4 = xtmp3[:]
                        xtmp4.append(d)
                        # check if game ends
                        if checkend(xtmp4):
                            tmp.append(xtmp4)
                            continue
        
                        # function to iterate fifth turn possibilities
                        for e in p(d):
                            xtmp5 = xtmp4[:]
                            xtmp5.append(e)
                            # check if game end
                            if checkend(xtmp5):
                                tmp.append(xtmp5)
                                continue
                        
                            # function to iterate sixth turn possibilities
                            for f in p(e, token=-1):
                                xtmp6 = xtmp5[:]
                                xtmp6.append(f)
                                # check if game ends
                                if checkend(xtmp6):
                                    tmp.append(xtmp6)
                                    continue
                            
                            
                                # function to iterate seventh turn possibilities
                                for g in p(f):
                                    xtmp7 = xtmp6[:]
                                    xtmp7.append(g)
                                    # check if game ends
                                    if checkend(xtmp7):
                                        tmp.append(xtmp7)
                                        continue
        
                                    # function to iterate eight turn possibilities
                                    for h in p(g, token=-1):
                                        xtmp8 = xtmp7[:]
                                        xtmp8.append(h)
                                        # check if game end
                                        if checkend(xtmp8):
                                            tmp.append(xtmp8)
                                            continue
        
        
                                        # function to iterate ninth turn possibilities
                                        for i in p(h):
                                            xtmp9 = xtmp8[:]
                                            xtmp9.append(i)
                                            tmp.append(xtmp9)
        
        # return dataset
        return tmp




# main function
def main(path):
    print "[*] Press Enter To Continue.. \n[*] It Will Take little Time To Complete...."
    raw_input('...')
    
    # Generate Dataset 
    dataset = GenerateDataset()
    print "[*] Data Generation Process Complete.."
    print "[*] Total Possibile Situation Generated : ", len(dataset)
    print "[*] Example Situation, Our Player [X] "
    
    # print random winning situation
    print "[*] Random Win Conditions Picked From Dataset."
    pretifyboard(random.choice(dataset.selfwin()))
    
    #
    for i in arrange_dataset([dataset.won[0]]):
        pretifyboard(i)
    print "[*] Time To Filter And Setup All Data Into A File."
   
    print "[*] Dataset Winning Possibilities Length  : ", len(dataset.won)
    print "[*] Dataset Fastest Winning Possibilities : ", len(dataset.won[0])
    print "[*] Dataset Last End Winning Possibility  : ", len(dataset.won[-1])

    with DatasetCollecter(filepath=path) as dwrite:
        for row in dataset.won[:70000]:
            for a,b in arrange_dataset([row]):
                dwrite[a]=b

        # Don't Trained for draw
        for row in dataset.draw[:1]:
            for a,b in arrange_dataset([row]):
                dwrite[a]=b
        #print dwrite
                
    return


# Trigger
if __name__=='__main__':
    main('../tmp/generated_dataset.csv')
