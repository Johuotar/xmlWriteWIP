#python 3.6
import csv
import xml.etree.ElementTree as ET
import os#dir paths

csvloop = 0#csv loop amount

script_dir = os.path.dirname(__file__)
rel_csv_path = "csvsource.txt"
abs_csv_path = os.path.join(script_dir, rel_csv_path)
csvfile = open(abs_csv_path,"r")
csvlist = csvfile.read().splitlines()
dictExists = False

UpperDictionary = {}#All dictionaries go to this dict
i=1
while (csvloop < len(csvlist)):#stop when csv list completed
        #loop to get all conditions from csv
        for row in csvlist:
    
            with open(csvlist[csvloop], "r") as file:
                fileReader = csv.reader(file, delimiter=';', quotechar='|')
                print("opened " + csvlist[csvloop])
                csvloop = csvloop+1
                print("csvloop value: " + str(csvloop))

                for row in fileReader:
                        for col in row:

                                if " id" in col:
                                        print("ID column found!")
                                        IdCol = row.index(col)#ID Column
                                
                                if " class" in col:
                                        
                        #column number needs to be placed in variable that is used in next part
                                        print("Row which contains 'class' found, it contains: " + col)
                                        if i == 1:
                                                Class1 = col#Class variables = string with class names
                                                a = row.index(col)#a, b & c are the index numbers of col                             if i == 2:
                                                Class2 = col
                                                b = row.index(col)
                                        if i == 3:
                                                Class3 = col
                                                c = row.index(col)
                                        i=i+1#class and annotation append to list. ID is the key
                                        print(row.index(col))#Need to know column for row[x] used below
                                        
                        if row[0] not in "sentence id":
                                 if row[a] or row[b] or row[c] not in "":#rows with no annotations skip
                                     AnnotationID = row[IdCol]#column of ID's
                                     if dictExists == False:
                                             dictExists = True
                                             AnnoDict = { AnnotationID : []}
                                     
                                     AnnoDict[AnnotationID].append((Class1, row[a]))#KEY ERROR, mayby trying to add duplicates
                                     AnnoDict[AnnotationID].append((Class2, row[b]))
                                     AnnoDict[AnnotationID].append((Class3, row[c]))
                                     
                                     
                print(AnnoDict) #Lets see what the final result is...
