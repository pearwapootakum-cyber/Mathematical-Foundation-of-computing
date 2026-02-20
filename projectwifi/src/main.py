from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# ใส่ API KEY ตรงนี้
API_KEY = "PUT_YOUR_API_KEY_HERE"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_location", methods=["POST"])
def get_location():

    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={API_KEY}"

    response = requests.post(url, json={})
    result = response.json()

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)