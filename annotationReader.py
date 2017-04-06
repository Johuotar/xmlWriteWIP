#Python 3.6
import csv as CS
import xml.etree.ElementTree as ET
import os
import NewCsvReaderTest2
from NewCsvReaderTest2 import AnnoDict
#cd C:\Users\jmfhuo\Desktop\xmlWriteWIP\
#py annotationReader.py csvsource.txt
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

    for node in root.findall('.//Sentence'):
        if node.attrib['sentence_id']:
            #Sentence node with sentence_id found!
            if node.attrib['sentence_id'] in AnnoDict:
                print("AnnoDict has same attr:")
                print(node.attrib['sentence_id'])#id shared with Dict
                print(AnnoDict[node.attrib['sentence_id']])#prints tuple
                CurTuple = AnnoDict[node.attrib['sentence_id']]
                print(CurTuple)
                print(len(CurTuple))
                a, = CurTuple
                
                sub = ET.SubElement(node, a)
                print("what is a?")
                print(a)
                sub.text = b
                #tag = SubElement(node,'TagName')
                #tag.attrib['attr'] = 'AttribValue'
                #compare id to AnnoDict id's get related annotations
                #add annotations to node
        
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
