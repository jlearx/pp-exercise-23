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
            num = int(line)
            numList.append(num)
            line = open_file.readline()   
    
    return numList

def getOverlapSets(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    overlap = list(set1 & set2)
    
    return overlap

if __name__ == '__main__':
    happyFile = "../happynumbers.txt"
    primeFile = "../primenumbers.txt"
    
    happyNums = readFile(happyFile)
    primeNums = readFile(primeFile)
    overlap = getOverlapSets(happyNums, primeNums)
    
    print("The Happy Numbers are:")
    print(happyNums)
    print("The Prime Numbers are:")
    print(primeNums)
    print("Overlap between the two sets of numbers:")
    print(overlap)
    