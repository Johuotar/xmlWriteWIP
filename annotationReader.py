import csv
import xml.etree.ElementTree as ET
import os
import NewCsvReaderTest
from NewCsvReaderTest import UpperDictionary
#Python 3.6
xmlloop = 0#xml loop amount


script_dir = os.path.dirname(__file__)
rel_xml_path = "xmlsource.txt"
abs_xml_path = os.path.join(script_dir, rel_xml_path)

xmlfile = open(abs_xml_path,"r")
xmllist = xmlfile.read().splitlines()
AnnoList = []
KeyList = []

print("lenght of xml list "+ str(len(xmllist)))
while (xmlloop < len(xmllist)):#stop when all xml files ready
    tree = ET.parse(xmllist[xmlloop])
    print(xmllist[xmlloop] + " parsed to tree")
    root = tree.getroot()
    xmlloop = xmlloop + 1
    print("xmlloop value: " + str(xmlloop))

    for key in UpperDictionary:
        print("looking for: " + str(key))
        data = root.find(key)#Never finds the key because is looking for solmu type (<Title>)
        #ID number is attribute type, cant find with root.find(x)
        #print(UpperDictionary[key])#Row by row show the existing annotations
        if data != None:
            print("SUCCESSFUL FIND!")
            for k, v in UpperDictionary[key].items():
                KeyList.append(k)
                AnnoList.append(v)
            print(KeyList)
            print(AnnoList)
            print(data)
        
            sub1 = ET.SubElement(data, KeyList[0])
            sub1.text = AnnoList[0]
            sub2 = ET.SubElement(data, KeyList[1])
            sub2.text = AnnoList[1]
            sub3 = ET.SubElement(data, KeyList[2])
            sub3.text = AnnoList[2]
        
        rel_dir_path = r"results\xmlresult{0}.txt".format(xmlloop)
        abs_dir_path = os.path.join(script_dir, rel_dir_path)
        #.format to make the filenames
                                
        tree.write(abs_dir_path,encoding="UTF-8")
        
        print(abs_dir_path)
        
xmlfile.close()
print("file closed")
