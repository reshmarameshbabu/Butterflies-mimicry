import xml.etree.ElementTree as ET
import argparse

# parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Path to the input XML file")
parser.add_argument("output_file", help="Path to the output XML file")
args = parser.parse_args()

# parse the XML file
tree = ET.parse(args.input_file)
root = tree.getroot()

# loop through each image element
for image in root.findall("./images/image"):
    # get the height of the box
    box_height = int(image.find("./box").attrib["height"])
    
    # loop through each part element
    for part in image.findall("./box/part"):
        # get the x coordinate of the part
        y = int(part.attrib["y"])
        
        # modify the x coordinate using the formula
        y = box_height - y
        
        # update the x coordinate in the XML file
        part.attrib["y"] = str(y)

# write the updated XML tree to a file
tree.write(args.output_file)