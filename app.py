import xml.etree.ElementTree as ET

person = ET.Element("person")

ET.SubElement(person, "name").text = input("Name: ")
ET.SubElement(person, "age").text = input("Age: ")

tree = ET.ElementTree(person)

tree.write("person.xml")