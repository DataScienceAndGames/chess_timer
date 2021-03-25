import sys
import time
import threading
import logging

def some_positive(arr):
    all_zeros = True
    for player in arr:
        
        for i in player:
            if i>=0:
                all_zeros = False
    return not all_zeros

def some_negative(arr):
    for player in arr:
        if player[0]<0:
            return True
    return False

def one_down(tup):
    if tup[1]<=0:
        tup[0]-=1
        tup[1] = 59.9
    else:
        tup[1]-=0.1
    return tup

class Over:
    def __init__(self):
        self.isOver = False
over = Over()

class Turn:
    def __init__(self):
        self.active = 0
turn = Turn()

def time_down():    
    times = [[0,10.0],[0,10.0]]
    turn.active = 0
    while(not some_negative(times)):
        times[turn.active] = one_down(times[turn.active])
        sys.stdout.write(f"White time: {times[0][0]}:{round(times[0][1],1)}\tBlack time: {times[1][0]}:{round(times[1][1],1)}\r" )
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    if(times[0][0]<0):
        print("White loses by time!")
    if(times[1][0]<0):
        print("Black loses by time!")
    over.isOver = True

x = threading.Thread(target=time_down)
x.start()
while (not over.isOver):
    input("")
    if(turn.active == 0):
        turn.active = 1
    else:
        turn.active = 0

    

