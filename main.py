import folium
import pandas

data = pandas.read_csv("4.1 Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
nam = list(data["NAME"])
elev = list(data["ELEV"])


def color_producer(op):
    if op == "---":
        return "green"
    elif op <= "400":
        return "orange"
    else:
        return "red"


map = folium.Map(location=[12.2958,76.6394] , zoom_start=6, tiles="cartodbdark_matter")

fg = folium.FeatureGroup(name="Volcanoes in India")
for lt, ln, nm, el in zip(lat, lon, nam, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], popup=(el + "m"), tooltip=(nm), radius=6, fill_color = color_producer(str(el)), color='grey', fill_opacity= 0.7))
pm = folium.FeatureGroup(name="Population Stats")
pm.add_child(folium.GeoJson(data = (open('world.json', 'r', encoding='utf-8-sig')).read(),
                            style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 100000000
else 'orange' if 100000000 <= x['properties']['POP2005'] < 250000000 else 'red'}))


map.add_child(fg)
map.add_child(pm)
map.add_child(folium.LayerControl())
map.save("Mys.html")