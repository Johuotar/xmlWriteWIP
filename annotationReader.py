#Python 3.6
import csv
import xml.etree.ElementTree as ET
import os
import NewCsvReaderTest2
from NewCsvReaderTest2 import AnnoDict

script_dir = os.path.dirname(__file__)
rel_xml_path = "xmlsource.txt"
abs_xml_path = os.path.join(script_dir, rel_xml_path)

xmlfile = open(abs_xml_path,"r")
xmllist = xmlfile.read().splitlines()
AnnoList = []
KeyList = []

#while (xmlloop < len(xmllist)):#stop when all xml files ready
for xml in xmllist:
    tree = ET.parse(xml)
    print(xml + " parsed to tree")
    root = tree.getroot()

    for key in AnnoDict:
        print("looking for: " + str(key))
        data = root.find(key)#Never finds the key because is looking for solmu type (<Title>)
        #ID number is attribute type, cant find with root.find(x)
        if data != None:
            print("Appending to lists")
            for k, v in AnnoDict[key].items():
                KeyList.append(k)
                AnnoList.append(v)
            print(KeyList)
            print(AnnoList)
            print(data)

            for a, b in enumerate(AnnoDict):
                
                sub = ET.SubElement(data, a)
                sub.text = b
                
                
        rel_dir_path = r"results\xmlresult{0}.txt".format(xmlloop)#cant use xmlloop var
        abs_dir_path = os.path.join(script_dir, rel_dir_path)
        #.format to make the filenames
                                
        tree.write(abs_dir_path,encoding="UTF-8")
        
        print(abs_dir_path)
        
xmlfile.close()
print("file closed")
