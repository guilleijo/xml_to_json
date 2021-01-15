import os
import xml.etree.ElementTree as ET


class ParseException(Exception):
    pass


def process_tree(tree, name):
    """
    Recursive function to go through the tree creating dicts
    """
    children = tree.getchildren()
    if not children:
        return {tree.tag: tree.text}

    new_object = {name: []}
    for child in children:
        processed_node = process_tree(child, child.tag)
        new_object[name].append(processed_node)

    return new_object


def convert_xml_to_json(xml_file):
    try:
        tree = ET.parse(xml_file)
    except ET.ParseError:
        raise ParseException('Invalid file, please select a valid XML file.')

    file_name = os.path.basename(xml_file.name).capitalize()
    root = tree.getroot()

    children = root.getchildren()
    if children:
        return process_tree(root, file_name)

    return {'Root': ''}
