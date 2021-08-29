import xml.sax
from xml.sax import handler

class PeopleHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if name == "person":
            print(f"-- person {attrs['id']} --")
    
    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content

    def endElement(self, name):
        if self.current == "name":
            print(f"name: {self.name}")
        elif self.current == "age":
            print(f"name: {self.age}")
        elif self.current == "weight":
            print(f"name: {self.weight}")
        elif self.current == "height":
            print(f"name: {self.height}")
        self.current = ""

handler = PeopleHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('people.xml')