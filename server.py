from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import requests

app = Flask(__name__, static_folder='.')
CORS(app)

API_KEY = "AIzaSyBATkrP7p3patEzCpnBtcz4XvodGEftYQo"  # <-- INSERT your real Google Places API key here

@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'coffee_fixed.html')

@app.route('/places')
def places():
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    if not lat or not lng:
        return jsonify({'error': 'Missing lat/lng'}), 400

    url = (
        f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        f"?location={lat},{lng}&radius=1500&type=cafe&keyword=coffee&key={API_KEY}"
    )

    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
