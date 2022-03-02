import sys
import csv

if len(sys.argv) != 3:
    print(exit)
    sys.exit("Error: Usage\n two files needed")

#read csv file into the memory as csvDna
with open('sys.argv[1]') as csvFile:
    csvRead = csv.reader(csvFile, delimiter = ',')
    for row in csvRead:
        csvDna = row
        csvDna.pop(0) #to delete the first row which is just a header 
        break
        
#read sequence file into the memory
with open('sys.argv[2]') as sequenceFile:
    sequenceRead = csv.reader(sequenceFile)
    for row in sequenceRead:
        sequenceList = row
        dna = sequenceList[0] #creating a string to store the sequences
        sequence = {} #creating a dictionary to store counted sequences later
        
for items in csvDna:
    csvDna[items] = 1 #copy the list in a dictionary where genes are the key