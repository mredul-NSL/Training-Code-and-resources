port sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    res = 0
    for i in node.iter():
        res += len(i.attrib)
        
    return res

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))