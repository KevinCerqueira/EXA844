from dom_parser import DOMParser
from sax_parser import SAXParser
import json

file_path = str(input("Insira o nome do arquivo (padrão: map): \n >> "))

if(file_path == ""):
    file_path = "map.osm"
elif(file_path.count('.osm') == 0):
    file_path += ".osm"

dom = DOMParser(file_path)
sax = SAXParser(file_path)
dom_time = dom.get_time()
sax_time = sax.get_time()

print(f"\n\n------------------------------- \n> DOM Time: {dom_time} \n> SAX Time: {sax_time} \n -------------------------------")

features = []
for e in sax.get_data():
    feature = {
        'type': 'Feature',
        'properties': {
            'tipo': e['tipo'],
            'nome': e['nome']
        },
        'geometry': {
            'type': 'Point',
            'coordinates': [e['longitude'], e['latitude']]
        }
    }
    features.append(feature)

geojson = {
    'type': 'FeatureCollection',
    'features': features
}

with open('estabelecimentos.geojson', 'w') as f:
    json.dump(geojson, f)