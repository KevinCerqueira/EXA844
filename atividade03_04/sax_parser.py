# Parser SAX
import xml.dom.minidom
import xml.sax
import time

class OSMHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.est_type = None
        self.name = None
        self.data = []

    def startElement(self, name, attrs):
        if name == 'node':
            self.latitude = attrs.get('lat')
            self.longitude = attrs.get('lon')
        elif name == 'tag':
            if attrs.get('k') == 'amenity':
                self.est_type = attrs.get('v')
            elif attrs.get('k') == 'name':
                self.name = attrs.get('v')

    def endElement(self, name):
        if name == 'node' and self.est_type is not None and self.name is not None:
            self.data.append({"latitude": float(self.latitude), "longitude": float(self.longitude), "tipo": str(self.est_type), "nome": str(self.name)})
            print(f"Latitude: {self.latitude}, Longitude: {self.longitude}, Tipo: {self.est_type}, Nome: {self.name}")
            self.latitude = None
            self.longitude = None
            self.est_type = None
            self.name = None
        
    
class SAXParser:
    
    def __init__(self, file_path):
        print("-- STARTING SAX PARSE")
        self.handler = OSMHandler()
        start_time = time.time()
        parser = xml.sax.make_parser()
        parser.setContentHandler(self.handler)
        parser.parse(file_path)
        time_process = time.time() - start_time
        print("-- TIME PROCESS: ", time_process)
        self.time = time_process
        
    def get_time(self):
        return self.time
    
    def get_data(self):
        return self.handler.data