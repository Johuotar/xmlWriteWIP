#Python 3.6
import csv as CS
import xml.etree.ElementTree as ET
import os
import csvReader
from csvReader import AnnoDict
import indent as IND
#cd C:\Users\jmfhuo\Desktop\xmlWriteWIP\
#py xmlWriter.py csvsource.txt
script_dir = os.path.dirname(__file__)
rel_xml_path = "xmlsource.txt"
abs_xml_path = os.path.join(script_dir, rel_xml_path)

xmlfile = open(abs_xml_path,"r")
xmllist = xmlfile.read().splitlines()

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
                print(AnnoDict[node.attrib['sentence_id']])
                CurDict = AnnoDict[node.attrib['sentence_id']]
                for Tupl in CurDict:
                    a, b = Tupl
                    print(a + b)
                    sub = ET.SubElement(node, 'Annotation')
                    sub.set('type', a)
                    sub.text = b
                    print("finished one loop of xml writing")
                    #imported function, indent
                    IND.indent(root)
    xmlName = xml.split("\\")[-1]
    print(xmlName)
    res_path = os.path.join('Results', xmlName)
    tree.write(res_path,encoding="UTF-8")
    print(res_path)
xmlfile.close()
print("xmlfile closed")


if __name__ == '__main__':
    pass
#funktio kutsut
