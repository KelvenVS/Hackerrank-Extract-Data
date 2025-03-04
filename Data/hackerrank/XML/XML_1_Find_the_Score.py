
number = 0
def get_attr_number(node):
    global number
    number = len(node.attrib)
    for child in node:
        number += get_attr_number(child)
    return number;
    
