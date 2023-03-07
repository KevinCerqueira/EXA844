from dom_parser import DOMParser
from sax_parser import SAXParser
import geojson


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

with open('dom_estabelecimentos.geojson', 'w') as f:
    feature_collection = geojson.FeatureCollection([])

    for estabelecimento in dom.get_data():
        feature = geojson.Feature(geometry=geojson.Point((estabelecimento['longitude'], estabelecimento['latitude'])), properties={"tipo": estabelecimento['tipo'], "nome": estabelecimento['nome']})
        feature_collection['features'].append(feature)

    geojson.dump(feature_collection, f)
print("\n-- GENERATED DOM GEOJSON")

with open('sax_estabelecimentos.geojson', 'w') as f:
    feature_collection = geojson.FeatureCollection([])

    for estabelecimento in sax.get_data():
        feature = geojson.Feature(geometry=geojson.Point((estabelecimento['longitude'], estabelecimento['latitude'])), properties={"tipo": estabelecimento['tipo'], "nome": estabelecimento['nome']})
        feature_collection['features'].append(feature)

    geojson.dump(feature_collection, f)
print("\n-- GENERATED SAX GEOJSON")