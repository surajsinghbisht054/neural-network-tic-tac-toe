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


#  import modules
import os
from src.conditions import pretifyboard, getaval
from pybrain.tools.xml import NetworkReader
from src.conditions import checkend
import random

PATH = '/home/suraj/Desktop/Projects/neural-network-tic-tac-toe/tmp/computed_weight.weight'


class TicTacToe:
    def __init__(self, path):
        self.weight = NetworkReader.readFrom(path)

        self.gameboard = [0,0,0,0,0,0,0,0,0]
        
        # time to add random input
        self.gameboard.append(random.randrange(-99,99)*0.01)
        
        self.startgame()
        self.turn = 0
        
    def demo(self):
        print """
___________________________________
     Board Index Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   0 | 1 | 2
 -------------
   3 | 4 | 5
 -------------
   6 | 7 | 8 
        
__________________________________         
    | Current Game Status |
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        """
        return
        
        
    def startgame(self):
        self.turn = 1
        self.invoke = 9
        
        while self.invoke:
            os.system('clear')
            self.demo()
            pretifyboard([self.gameboard])
            self.takeinput()
            
            if self.turn==1:
                self.turn=-1
            else:
                self.turn=1
            if checkend([self.gameboard], token=1):
                return
            if checkend([self.gameboard], token=-1):
                return
            self.invoke-=1
        
        return
    def takeinput(self):
        if self.turn==1:
            # computer
            print "[*] Computers Turn"
            answer = self.weight.activate(self.gameboard)
            think = {}
            gv = getaval(self.gameboard[:9])
            for index, probability in enumerate(answer):
                if index not in gv:
                    continue
                think[index]=probability
            #print think
            self.gameboard[keywithmaxval(think)]=-1
            print "[*] Computer Choice : ",keywithmaxval(think)
        else:
            # player
            print "[*] Player Turn"
            self.gameboard[int(raw_input("[-] Your Replay ? : "))]=1
        return
    
def keywithmaxval(d):
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]

    
def main():
    g = TicTacToe(PATH)
    return

#main()


# Trigger
if __name__=='__main__':
    main()
