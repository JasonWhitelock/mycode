from flask import Flask

import folium

app = Flask(__name__)

# HTTP GET /
# create a map that returns hershey 
@app.route('/')
def index():
    start_coords = (40.284, -76.649)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()

# HTTP GET /kansascity
# create a map that returns a display of kansas city
@app.route('/kansascity')
def kansascity():
    start_coords = (39.099, -94.578)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()

# HTTP GET /home
# map that returns kinnaird village
@app.route('/home')
def home():
    start_coords = (56.038, -3.824)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()

# HTTP GET /disney
# map that returns disney
@app.route('/disney')
def disney():
    start_coords = (28.418718, -81.581210)
    folium_map = folium.Map(location=start_coords, zoom_start=16)
    # Define the coordinates we want our markers to be at
    CC = [28.416522, -81.580943]     # where christian collapsed
    FA = [28.416995, -81.581747]   # First Aid Room
    FO = [28.420355, -81.580869]  # Super fountain
    # Add markers to the map
    # popup --> label for the Marker; click on the pins on the map!
    folium.Marker(CC, popup = 'Christian Fainted').add_to(my_map)
    folium.Marker(FA, popup = 'First Aid Room').add_to(my_map)
    folium.Marker(FO, popup = 'The favourite fountain').add_to(my_map)
    return folium_map_.repr_html_()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224, debug=True)
