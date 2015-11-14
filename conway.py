#!/usr/local/bin/python2.7
import os
import sys
import random
import time

class game(object):
    def __init__(self):
        self.map_1 = [[0,0,0,1,0,0,0,0,0], [0,0,1,1,0,0,0,0,0]]

    def next(self, own, neighbor):
        return self.map_1[own][neighbor]

def main():
    row = 36
    col = 80
    map = [[0 for i in range(col)] for i in range(row)]
    for i in range(row):
        for j in range(col):
            if i==0 or i==row-1 or j==0 or j==col-1 : map[i][j] = 0
            else :
                if random.random() > 0.5 : map[i][j] = 1
                else : map[i][j] = 0

    a = game()

    while True:
        map_new = [[0 for i in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                if i==0 or i==row-1 or j==0 or j==col-1 : continue
                own = map[i][j]
                neighbor = map[i-1][j-1] + map[i-1][j] + map[i-1][j+1] + map[i][j-1] + map[i][j+1] + map[i+1][j-1] + map[i+1][j] + map[i+1][j+1]
                map_new[i][j] = a.next(own, neighbor)
        map = map_new
        for i in range(row):
            print_str = ""
            for j in range(col):
                if map[i][j] : cell = "*"
                else : cell = " "
                print_str += cell
            print print_str
        time.sleep(0.2)
        os.system('clear')
        print "Row : " + str(row) + " Col : " + str(col)

if __name__ == "__main__":
    main()
