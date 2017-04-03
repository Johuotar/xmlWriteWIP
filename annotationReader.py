#Python 3.6
import csv as CS
import xml.etree.ElementTree as ET
import os
import NewCsvReaderTest2
from NewCsvReaderTest2 import AnnoDict

script_dir = os.path.dirname(__file__)
rel_xml_path = "xmlsource.txt"
abs_xml_path = os.path.join(script_dir, rel_xml_path)
res_xml_path = os.path.join(script_dir, "Results\\")

xmlfile = open(abs_xml_path,"r")
xmllist = xmlfile.read().splitlines()
#AnnoList = []
#KeyList = []


for xml in xmllist:
    tree = ET.parse(xml)
    print(xml + " parsed to tree")
    root = tree.getroot()

    for node in root.findall("sentence_id"):
        print("found sentence_id")
        final_path = os.path.join(res_xml_path, xml)               
        tree.write(final_path,encoding="UTF-8")
        print(final_path)
xmlfile.close()
print("xmlfile closed")

'''
    for key in AnnoDict:
        print("looking for: " + str(key))
        data = root.find(key)#Never finds the key because is looking for tag (<Title>)
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
'''
