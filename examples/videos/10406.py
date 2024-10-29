import xml.etree.ElementTree as ET

def parse_xml(file_path):
    # Load the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Extract data from the XML
    data = {}
    for child in root:
        # Each child is an element, extract name and value
        data[child.tag] = child.text
    return data

def main():
    input_file = '/tmp/test/input.xml'  # Path to your XML file
    xml_data = parse_xml(input_file)

    print("Parsed XML Data:")
    for key, value in xml_data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()