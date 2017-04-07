# -*- coding: utf-8 -*-

#### description

# function to create pretty indentation for ElementTree objects



#### helper functions

def getSpace():
    return("  ")

def indent(elem, level=0):
    """
    In-place indentation of XML (in cElementTree.Element object).
    This function was provided by Filip Salomonsson. See
    http://infix.se/2007/02/06/gentlemen-indent-your-xml.
    """
    i = "\n" + level*getSpace()
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + getSpace()
        for e in elem:
            indent(e, level+1)
            if not e.tail or not e.tail.strip():
                e.tail = i + getSpace()
        if not e.tail or not e.tail.strip():
            e.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i



#### main function

if __name__=='__main__':
    import sys as S
    import xml.etree.cElementTree as ET
    #
    xml = ET.parse(S.argv[1])
    indent(xml.getroot())
    xml.write(S.argv[1]+".indented", 'utf-8')
