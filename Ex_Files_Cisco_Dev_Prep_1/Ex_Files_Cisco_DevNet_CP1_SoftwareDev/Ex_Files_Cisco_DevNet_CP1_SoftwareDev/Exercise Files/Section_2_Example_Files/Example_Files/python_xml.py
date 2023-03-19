#!/usr/env/bin python
import xml.etree.ElementTree as ET
from pprint import pprint as pp

# import data
tree = ET.parse('NX-API_show_version.xml')

# get root element and print tag and attributes
root = tree.getroot()

pp("Root Tag: {} and Root Attribute: {}".format(root.tag, root.attrib))

# loop over children nodes and print their tag and attributes
pp("*" * 10)
pp("These are the children of root:")
for child in root:
    tag = child.tag
    attribute = child.attrib
    text = child.text
    pp(f"tag: {tag}, attrib: {attribute}, text: {text}")

# iterate over interesting element, such as 'output' by position
pp("*" * 10)
pp("These are the children of output:")
pp("iterate over fourth child of outputs and its first child of output")
for item in root[3][0].iter():
    tag, text = item.tag, item.text
    pp(f"tage: {tag}, text: {text}")

# iterate over and match element tags
pp("*" * 10)
pp("Find Nexus version by matching Element Tag:")
for item in root[3][0].iter():
    if item.tag == 'nxos_ver_str':
        version = item.text
        pp(f"Nexus is running version {version}")

# iterate over element by findall
for output in root.findall('outputs'):
    for element in output.iter():
        pp(element.tag)

