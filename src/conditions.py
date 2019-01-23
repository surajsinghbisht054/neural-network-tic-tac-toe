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

# Get Available Positions Index
def getaval(dataset):
    return [n for n,i in enumerate(dataset) if i==0] 

# check if game ends or not
def checkend(brd, token=1):
    #
    # 0 1 2
    # 3 4 5
    # 6 7 8
    #
    if win(brd[-1][:], token=token):
        return True

    if 0 in brd[-1]:
        return False

    else:
        return True


# possibilities generating function
def p(l, token=1):
    tmp = []
    for i in getaval(l):
        xtmp = l[:]
        xtmp[i] = token
        tmp.append(xtmp)
    
    return tmp

# function to check, game winning status
def win(brd, token=1):
    #
    # 0 1 2
    # 3 4 5
    # 6 7 8
    #
    if (
        (brd[0]==brd[1]==brd[2]==token)or
        (brd[3]==brd[4]==brd[5]==token)or
        (brd[6]==brd[7]==brd[8]==token)or
        (brd[0]==brd[3]==brd[6]==token)or
        (brd[1]==brd[4]==brd[7]==token)or
        (brd[2]==brd[5]==brd[8]==token)or
        (brd[0]==brd[4]==brd[8]==token)or
        (brd[2]==brd[4]==brd[6]==token)):
        #print "True"
        #print brd
        return True

    return False

# print beautiful game board
def pretifyboard(l):
    f="""
    
    {} | {} | {}
    ----------
    {} | {} | {}
    ----------
    {} | {} | {}
    
    """
    for c in l:
        tmp = f.format(*c)
        tmp = tmp.replace('-1', 'O')
        tmp = tmp.replace('1', 'X')
        tmp = tmp.replace('0', ' ')
        print tmp
    return

# creating demo situation
def main():

    # Player 1 is Won
    s =[
             -1, -1,  1,
              0,  1, -1,
              1,  0,  1,
            ]

    if win(s):
        print "[+] Game Player 1 Won This Match"
        pretifyboard([s])

    return

# Trigger
if __name__=='__main__':
    main()
