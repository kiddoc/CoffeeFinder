from flask import Flask, request, jsonify, send_from_directory, render_template_string
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = "AIzaSyBATkrP7p3patEzCpnBtcz4XvodGEftYQo"  # Keep it only here!

@app.route('/')
def index():
    html_content = open("coffee.html", encoding="utf-8").read()
    html_content = html_content.replace("GOOGLE_MAPS_API_KEY", API_KEY)  # Replace placeholder
    return render_template_string(html_content)




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
