
from flask import Flask, request, jsonify, render_template_string, make_response
import requests
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Use environment variable for security
API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY", "MISSING_KEY")

@app.route('/')
def index():
    with open("coffee.html", encoding="utf-8") as f:
        html = f.read()
    html = html.replace("GOOGLE_MAPS_API_KEY", API_KEY)

    response = make_response(render_template_string(html))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
