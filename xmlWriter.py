#Python 3.6
import sys as S
import collections as C
import csv as CS
import xml.etree.ElementTree as ET
import os  # dir paths
import indent as IND

#cd C:\Users\jmfhuo\Desktop\xmlWriteWIP\
#py xmlWriter.py csvsource.txt

def csvToXml():
    infile = S.argv[1]
    csvfile = open(infile, 'r')
    csvlist = [x.strip() for x in csvfile.readlines()]
    csvfile.close()

    AnnoDict = C.defaultdict(list)

    for csv in csvlist:
        print (csv)
        with open(csv, 'r') as file:
            fileReader = CS.reader(file, delimiter=';', quotechar='|')
            print ('opened ' + csv)

            header = next(fileReader)  # note Python 3 & 2 next differences
            while not 'sentence id' in header:
                next(header)

            IdCol = None
            AnnoCols = {}
            for (i, col) in enumerate(header):         

                if col.endswith(' id'):  # get id column index
                    print ('ID column found!')
                    IdCol = i

                if col.endswith(' class'):  # get annotation column indices
                    AnnoCols[i] = col[:-6]

            for row in fileReader:
                AnnotationID = row[IdCol]  # sentence id
                for anno_col in AnnoCols.keys():
                    if row[anno_col].strip():
                        AnnoDict[AnnotationID].append((AnnoCols[anno_col],
                                row[anno_col]))

            print (AnnoDict)  # print the resulting annotation dictionary

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
csvToXml()

