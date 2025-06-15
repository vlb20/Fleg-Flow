import json
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Dati GeoJSON (inserisci qui i tuoi dati)
geojson_data = {
  "type": "FeatureCollection",
  "generator": "overpass-turbo",
  "copyright": "The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.",
  "timestamp": "2025-06-12T15:35:15Z",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "@id": "node/325239246",
        "name": "Piave",
        "network": "Circumflegrea",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wheelchair": "limited",
        "wikidata": "Q3970473",
        "wikipedia": "it:Stazione di Piave"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.2065388,
          40.8429135
        ]
      },
      "id": "node/325239246"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/325240435",
        "name": "Soccavo",
        "network": "Circumflegrea",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wheelchair": "limited",
        "wikidata": "Q3971007",
        "wikipedia": "it:Stazione di Soccavo"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.2006167,
          40.8439578
        ]
      },
      "id": "node/325240435"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/325241055",
        "name": "Traiano",
        "network": "Circumflegrea",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wheelchair": "limited",
        "wikidata": "Q3971172",
        "wikipedia": "it:Stazione di Traiano"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1941085,
          40.8450687
        ]
      },
      "id": "node/325241055"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/325241710",
        "name": "La Trencia",
        "network": "Circumflegrea",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q3969897",
        "wikipedia": "it:Stazione di La Trencia"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1719378,
          40.8540341
        ]
      },
      "id": "node/325241710"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/326209133",
        "addr:city": "Arco felice",
        "addr:postcode": "80078",
        "addr:street": "Via Raimondo Anechinno",
        "internet_access": "no",
        "interval": "20",
        "name": "Arco Felice",
        "network": "Cumana",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wheelchair": "no",
        "wikidata": "Q3968891",
        "wikipedia": "it:Stazione di Arco Felice"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1015092,
          40.8328497
        ]
      },
      "id": "node/326209133"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/329653476",
        "name": "Licola",
        "network": "Circumflegrea",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q3969956",
        "wikipedia": "it:Stazione di Licola"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.0589519,
          40.8714621
        ]
      },
      "id": "node/329653476"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/329659352",
        "name": "Marina di Licola",
        "network": "Circumflegrea",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q3970049",
        "wikipedia": "it:Stazione di Marina di Licola"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.0480777,
          40.8631384
        ]
      },
      "id": "node/329659352"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/329701822",
        "name": "Bagnoli-Città della Scienza",
        "network": "Cumana",
        "operator": "EAV",
        "platforms": "2",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q3968948",
        "wikipedia": "it:Stazione di Bagnoli"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1667879,
          40.8151034
        ]
      },
      "id": "node/329701822"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/434789470",
        "name": "Mostra - Stadio Maradona",
        "network": "Cumana",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wheelchair": "yes",
        "wikidata": "Q3970236",
        "wikimedia_commons": "Category:Mostra train station",
        "wikipedia": "it:Stazione di Mostra-Stadio Maradona"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1932039,
          40.8245648
        ]
      },
      "id": "node/434789470"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/434789521",
        "name": "Agnano",
        "network": "Cumana",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q3968832",
        "wikipedia": "it:Stazione di Agnano"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1763585,
          40.8176973
        ]
      },
      "id": "node/434789521"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/663077724",
        "name": "Lala",
        "operator": "ANM",
        "public_transport": "station",
        "railway": "station",
        "station": "subway",
        "subway": "yes",
        "wikidata": "Q3826234",
        "wikipedia": "it:Lala (metropolitana di Napoli)"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.2045656,
          40.8268186
        ]
      },
      "id": "node/663077724"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/663078054",
        "name": "Mergellina",
        "operator": "ANM",
        "public_transport": "station",
        "railway": "station",
        "source": "it.wikipedia",
        "station": "subway",
        "subway": "yes",
        "wikidata": "Q3855118",
        "wikipedia": "it:Mergellina (metropolitana di Napoli)"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.2173675,
          40.830597
        ]
      },
      "id": "node/663078054"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/663078056",
        "name": "Augusto",
        "operator": "ANM",
        "public_transport": "station",
        "railway": "station",
        "station": "subway",
        "subway": "yes",
        "wheelchair": "no",
        "wikidata": "Q3629576",
        "wikipedia": "it:Augusto (metropolitana di Napoli)"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1983167,
          40.8261854
        ]
      },
      "id": "node/663078056"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/972220234",
        "name": "Pisani",
        "network": "Circumflegrea",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q3970501",
        "wikipedia": "it:Stazione di Pisani"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1435942,
          40.8652869
        ]
      },
      "id": "node/972220234"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1037516419",
        "name": "Quarto Officina",
        "network": "Circumflegrea",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q3970621",
        "wikipedia": "it:Stazione di Quarto Officina"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1259153,
          40.879101
        ]
      },
      "id": "node/1037516419"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1090940332",
        "layer": "-1",
        "name": "Fuorigrotta",
        "network": "Cumana",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wheelchair": "limited",
        "wikidata": "Q3969667",
        "wikipedia": "it:Stazione di Fuorigrotta"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.2017898,
          40.8279208
        ]
      },
      "id": "node/1090940332"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1338235385",
        "name": "Zoo-Edenlandia",
        "network": "Cumana",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q3971386",
        "wikipedia": "it:Stazione di Zoo-Edenlandia"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.183488,
          40.8203083
        ]
      },
      "id": "node/1338235385"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1338235386",
        "name": "Dazio",
        "network": "Cumana",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q3969513",
        "wikipedia": "it:Stazione di Dazio"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1600761,
          40.8172505
        ]
      },
      "id": "node/1338235386"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1338239162",
        "name": "Gerolomini",
        "network": "Cumana",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q3969723",
        "wikipedia": "it:Stazione di Gerolomini"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.135198,
          40.8206808
        ]
      },
      "id": "node/1338239162"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1462124085",
        "name": "Torregaveta",
        "operator": "EAV",
        "platforms": "4",
        "public_transport": "station",
        "railway": "station",
        "wikidata": "Q3971156",
        "wikipedia": "it:Stazione di Torregaveta"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.0448721,
          40.811495
        ]
      },
      "id": "node/1462124085"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1463003360",
        "name": "Grotta del Sole",
        "network": "Circumflegrea",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q3969759",
        "wikipedia": "it:Stazione di Grotta del Sole"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.0946728,
          40.8785138
        ]
      },
      "id": "node/1463003360"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1463010430",
        "name": "Cuma",
        "network": "Circumflegrea",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q3969501",
        "wikipedia": "it:Stazione di Cuma"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.0488298,
          40.8491369
        ]
      },
      "id": "node/1463010430"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1463010431",
        "name": "Lido Fusaro",
        "network": "Circumflegrea",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q3969958",
        "wikipedia": "it:Stazione di Lido Fusaro"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.0498377,
          40.8288802
        ]
      },
      "id": "node/1463010431"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1480005815",
        "name": "Lucrino",
        "network": "Cumana",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wheelchair": "no",
        "wikidata": "Q3969984",
        "wikipedia": "it:Stazione di Lucrino"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.0834472,
          40.8292497
        ]
      },
      "id": "node/1480005815"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6536935424",
        "name": "Napoli Mergellina",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wheelchair": "limited",
        "wikidata": "Q3970277",
        "wikipedia": "it:Stazione di Napoli Mergellina"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.2187034,
          40.8315681
        ]
      },
      "id": "node/6536935424"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6817740560",
        "name": "Napoli Campi Flegrei",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wheelchair": "no",
        "wikidata": "Q3970272",
        "wikipedia": "it:Stazione di Napoli Campi Flegrei"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1946381,
          40.8221756
        ]
      },
      "id": "node/6817740560"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6817755819",
        "name": "Bagnoli-Agnano Terme",
        "operator": "RFI",
        "platforms": "2",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wheelchair": "no",
        "wikidata": "Q3968951",
        "wikipedia": "it:Stazione di Bagnoli-Agnano Terme"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1666694,
          40.8194209
        ]
      },
      "id": "node/6817755819"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6817760441",
        "name": "Napoli Piazza Leopardi",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wheelchair": "no",
        "wikidata": "Q3970282",
        "wikipedia": "it:Stazione di Napoli Piazza Leopardi"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.199742,
          40.8240468
        ]
      },
      "id": "node/6817760441"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6817792727",
        "name": "Pozzuoli Solfatara",
        "public_transport": "station",
        "railway": "station",
        "wheelchair": "no",
        "wikidata": "Q3970598",
        "wikipedia": "it:Stazione di Pozzuoli Solfatara"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1260691,
          40.8276089
        ]
      },
      "id": "node/6817792727"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/7884684060",
        "name": "Mostra",
        "operator": "ANM",
        "public_transport": "station",
        "railway": "station",
        "station": "subway",
        "subway": "yes",
        "wikidata": "Q3866164",
        "wikipedia": "it:Mostra (metropolitana di Napoli)"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1936564,
          40.8243372
        ]
      },
      "id": "node/7884684060"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/8278678762",
        "name": "Cavalleggeri Aosta",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wheelchair": "no",
        "wikidata": "Q3969355",
        "wikipedia": "it:Stazione di Cavalleggeri Aosta"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.18763,
          40.8198824
        ]
      },
      "id": "node/8278678762"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/8748727887",
        "name": "Fusaro",
        "network": "Cumana",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q3969668",
        "wikipedia": "it:Stazione di Fusaro"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.0617293,
          40.8185701
        ]
      },
      "id": "node/8748727887"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9126513777",
        "addr:city": "Pozzuoli",
        "addr:housenumber": "230",
        "addr:street": "Via Campana",
        "name": "Via Campana",
        "operator": "RFI",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q33104084"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1206014,
          40.8533089
        ]
      },
      "id": "node/9126513777"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4936292644",
        "name": "Pianura",
        "network": "Circumflegrea",
        "operator": "EAV",
        "public_transport": "station",
        "railway": "station",
        "train": "yes",
        "wikidata": "Q3970470",
        "wikipedia": "it:Stazione di Pianura"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          14.1624307,
          40.8560001
        ]
      },
      "id": "node/4936292644"
    }
  ]
}

def create_transport_network_graph():
    # Creazione del grafo
    G = nx.Graph()
    
    # Estrazione delle stazioni ferroviarie/metro
    stations = []
    for feature in geojson_data['features']:
        props = feature['properties']
        # Filtra solo le stazioni di trasporto pubblico
        if ('public_transport' in props and props['public_transport'] == 'station' and 
            ('railway' in props or 'subway' in props)):
            
            name = props.get('name', 'Unknown')
            network = props.get('network', 'Unknown')
            operator = props.get('operator', 'Unknown')
            coords = feature['geometry']['coordinates']
            
            stations.append({
                'name': name,
                'network': network,
                'operator': operator,
                'lon': coords[0],
                'lat': coords[1],
                'wheelchair': props.get('wheelchair', 'unknown'),
                'subway': 'subway' in props and props['subway'] == 'yes'
            })
    
    # Organizzazione per rete
    networks = defaultdict(list)
    for station in stations:
        networks[station['network']].append(station)
    
    # Aggiunta nodi al grafo
    for station in stations:
        G.add_node(station['name'], 
                  network=station['network'],
                  operator=station['operator'],
                  pos=(station['lon'], station['lat']),
                  wheelchair=station['wheelchair'],
                  subway=station['subway'])
    
    # Connessione delle stazioni della stessa rete (semplificazione)
    # In realtà dovremmo avere le connessioni reali, ma creiamo collegamenti logici
    
    # Per la Circumflegrea, ordiniamo per posizione geografica approssimativa
    circumflegrea_stations = sorted(networks['Circumflegrea'], 
                                  key=lambda x: (x['lat'], x['lon']))
    for i in range(len(circumflegrea_stations) - 1):
        G.add_edge(circumflegrea_stations[i]['name'], 
                  circumflegrea_stations[i+1]['name'],
                  network='Circumflegrea')
    
    # Per la Cumana
    cumana_stations = sorted(networks['Cumana'], 
                           key=lambda x: x['lon'])  # Ordine est-ovest
    for i in range(len(cumana_stations) - 1):
        G.add_edge(cumana_stations[i]['name'], 
                  cumana_stations[i+1]['name'],
                  network='Cumana')
    
    # Connessioni speciali per metropolitana (ANM)
    metro_stations = [s for s in stations if s['operator'] == 'ANM']
    if len(metro_stations) > 1:
        # Collega le stazioni metro in sequenza logica
        metro_sorted = sorted(metro_stations, key=lambda x: x['lon'])
        for i in range(len(metro_sorted) - 1):
            G.add_edge(metro_sorted[i]['name'], 
                      metro_sorted[i+1]['name'],
                      network='Metro')
    
    # Connessioni inter-rete (scambi potenziali basati sulla vicinanza)
    for i, s1 in enumerate(stations):
        for s2 in stations[i+1:]:
            if s1['network'] != s2['network']:
                # Calcola distanza approssimativa
                dist = np.sqrt((s1['lon'] - s2['lon'])**2 + (s1['lat'] - s2['lat'])**2)
                if dist < 0.005:  # Soglia di vicinanza
                    G.add_edge(s1['name'], s2['name'], 
                              network='Interchange', 
                              weight=0.5)
    
    return G, networks

def visualize_network(G, networks):
    plt.figure(figsize=(16, 12))
    
    # Posizioni basate sulle coordinate geografiche
    pos = nx.get_node_attributes(G, 'pos')
    
    # Colori per le diverse reti
    network_colors = {
        'Circumflegrea': '#FF6B6B',
        'Cumana': '#4ECDC4', 
        'Metro': '#45B7D1',
        'Interchange': '#96CEB4',
        'Unknown': '#FFEAA7'
    }
    
    # Disegna gli archi per rete
    for network, color in network_colors.items():
        edges = [(u, v) for u, v, d in G.edges(data=True) 
                if d.get('network', 'Unknown') == network]
        if edges:
            nx.draw_networkx_edges(G, pos, edgelist=edges, 
                                 edge_color=color, width=2, alpha=0.7)
    
    # Disegna i nodi colorati per operatore
    node_colors = []
    node_sizes = []
    for node in G.nodes():
        network = G.nodes[node].get('network', 'Unknown')
        is_subway = G.nodes[node].get('subway', False)
        
        if network == 'Circumflegrea':
            node_colors.append('#FF6B6B')
        elif network == 'Cumana':
            node_colors.append('#4ECDC4')
        elif G.nodes[node].get('operator') == 'ANM':  # Metro
            node_colors.append('#45B7D1')
        else:
            node_colors.append('#FFEAA7')
        
        # Dimensione maggiore per stazioni metro
        node_sizes.append(800 if is_subway else 500)
    
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, 
                          node_size=node_sizes, alpha=0.8)
    
    # Etichette
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')
    
    plt.title('Rete di Trasporto Pubblico - Area Napoli Ovest/Campi Flegrei', 
              fontsize=16, fontweight='bold')
    
    # Leggenda
    legend_elements = [
        plt.Line2D([0], [0], color='#FF6B6B', lw=3, label='Circumflegrea'),