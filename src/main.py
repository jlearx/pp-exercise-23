'''
Created on Sep 15, 2017

@author: jlearx
'''

def readFile(filename):
    numList = []

    with open(filename, 'r') as open_file:
        line = open_file.readline()
        
        while line:
            line = line.rstrip('\n')
            CountItem(nameDict, line)
            line = open_file.readline()   

if __name__ == '__main__':
    happyFile = "../happynumbers.txt"
    primeFile = "../primenumbers.txt"
    happyNums = []
    primeNums = []
    overlap = []
    
     