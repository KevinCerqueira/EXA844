import xml.dom.minidom
import xml.sax
import time

class DOMParser:
    
    def __init__(self, file_path):
        self.data = []
        self.parse_dom(file_path)
    
    def parse_dom(self, file_path):
        print("-- STARTIG DOM PARSER")
        start_time = time.time()
        dom_tree = xml.dom.minidom.parse(file_path)
        nodes = dom_tree.getElementsByTagName('node')
        for node in nodes:
            latitude = node.getAttribute('lat')
            longitude = node.getAttribute('lon')
            tags = node.getElementsByTagName('tag')
            est_type = None
            name = None
            for tag in tags:
                if tag.getAttribute('k') == 'amenity':
                    est_type = tag.getAttribute('v')
                if est_type is not None and tag.getAttribute('k') == 'name':
                    name = tag.getAttribute('v')
            if est_type is not None and name is not None:
                self.data.append({"latitude": float(latitude), "longitude": float(longitude), "tipo": str(est_type), "nome": str(name)})
                print(f"latitude: {latitude}, longitude: {longitude}, tipo: {est_type}, nome: {name}")
        time_process = time.time() - start_time
        print("-- TIME PROCESS: ", time_process)
        self.time = time_process
        
    def get_time(self):
        return self.time
    
    def get_data(self):
        return self.data
