#python 3.6
import sys as S
import csv as CS
import collections as C
import xml.etree.ElementTree as ET
import os#dir paths

infile = S.argv[1]
csvfile = open(infile, "r")
csvlist = [x.strip() for x in csvfile.readlines()]
csvfile.close()

AnnoDict = C.defaultdict(list)

for csv in csvlist:
        print(csv)
        with open(csv, "r") as file:
                fileReader = CS.reader(file, delimiter=';', quotechar='|')
                print("opened " + csv)

                header = next(fileReader)#Python 3 has different kind of next
                while not "sentence id" in header:
                        next(header)

                IdCol = None
                AnnoCols = {}
                for i, col in enumerate(header):
                        # get id column index
                        if col.endswith(" id"):
                                print("ID column found!")
                                IdCol = i
                        # get annotation column indices
                        if col.endswith(" class"):
                                AnnoCols[i] = col[:-6]

                for row in fileReader:
                        AnnotationID = row[IdCol] # sentence id
                        for anno_col in AnnoCols.keys():
                                if row[anno_col].strip():
                                     print(AnnoCols[anno_col])
                                     print(row[anno_col])
                                     print("^These 2 go to tuple^")

                                     AnnoDict[AnnotationID].append((AnnoCols[anno_col], row[anno_col]))
                                            
                print(AnnoDict) #Lets see what the final result is
