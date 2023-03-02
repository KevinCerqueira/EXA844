import geojson
from dom_parser import DOMParser

file_path = str(input("Insira o nome do arquivo (padrão: map): \n >> "))

if(file_path == ""):
    file_path = "map.osm"
elif(file_path.count('.osm') == 0):
    file_path += ".osm"

dom = DOMParser(file_path)

with open('estabelecimentos.geojson', 'w') as f:

    feature_collection = geojson.FeatureCollection([])

    for estabelecimento in dom.get_data():
        feature = geojson.Feature(geometry=geojson.Point((estabelecimento['longitude'], estabelecimento['latitude'])), properties={"tipo": estabelecimento['tipo'], "nome": estabelecimento['nome']})
        feature_collection['features'].append(feature)

    geojson.dump(feature_collection, f)