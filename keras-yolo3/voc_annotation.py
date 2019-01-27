import xml.etree.ElementTree as ET
from os import getcwd

classes = ["1", "2", "3", "4", "5", "6", "7", "8"]


def convert_annotation(image_id, list_file):
    in_file = open('train/annotations/%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes :
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd=getcwd()


image_ids = open('imageids.txt').read().strip().split()
list_file = open('train.txt', 'w')
for image_id in image_ids:
    list_file.write('%s/train/images/%s.jpg'%(wd, image_id))
    convert_annotation(image_id, list_file)
    list_file.write('\n')
list_file.close()

