from flask import Flask, render_template, jsonify
from skyfield.api import load
from datetime import datetime
from skyfield.api import utc

app = Flask(__name__)

@app.route('/')
def index():
    eph = load('de421.bsp')
    
    celestial_bodies = {
        'Sun': eph['sun'],
        'Moon': eph['moon'],
        'Merkur': eph['mercury barycenter'],
        'Venüs': eph['venus barycenter'],
        'Dünya': eph['earth barycenter'],
        'Mars': eph['mars barycenter'],
        'Jüpiter': eph['jupiter barycenter'],
        'Satürn': eph['saturn barycenter'],
        'Uranüs': eph['uranus barycenter'],
        'Neptün': eph['neptune barycenter']
    }
    
    ts = load.timescale()
    now = datetime.utcnow()
    now_time = ts.utc(now.year, now.month, now.day, now.hour, now.minute, now.second)
    
    body_positions = {}
    
    for body_name, body in celestial_bodies.items():
        konum = body.at(now_time).observe(eph['earth']).apparent()
        rect_coords = konum.position.km
        x, y, z = rect_coords
        body_positions[body_name] = (x, y, z)
    
    return render_template('index.html', body_positions=body_positions)

@app.route('/getPlanetCoordinates')
def get_planet_coordinates():
    eph = load('de421.bsp')
    
    celestial_bodies = {
        'Sun': eph['sun'],
        'Moon': eph['moon'],
        'Merkur': eph['mercury barycenter'],
        'Venüs': eph['venus barycenter'],
        'Dünya': eph['earth barycenter'],
        'Mars': eph['mars barycenter'],
        'Jüpiter': eph['jupiter barycenter'],
        'Satürn': eph['saturn barycenter'],
        'Uranüs': eph['uranus barycenter'],
        'Neptün': eph['neptune barycenter']
    }
    
    ts = load.timescale()
    now = datetime.utcnow()
    now_time = ts.utc(now.year, now.month, now.day, now.hour, now.minute, now.second)
    
    body_positions = {}
    
    for body_name, body in celestial_bodies.items():
        konum = body.at(now_time).observe(eph['earth']).apparent()
        rect_coords = konum.position.km
        x, y, z = rect_coords
        body_positions[body_name] = (x, y, z)
    
    return jsonify(body_positions)

if __name__ == '__main__':
    app.run(debug=True)
