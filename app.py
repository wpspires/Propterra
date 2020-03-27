import json
import os
import requests
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
 
Maps_API_Key = os.environ.get("Maps_API_Key")
InitialMap = f"<iframe frameborder='0' src='https://www.google.com/maps/embed/v1/view?key={Maps_API_Key}&center=0,0' allowfullscreen>"

@app.route("/")
def index():
    return render_template("index.html", MapRender=InitialMap)

@app.route("/calculate", methods=['POST'])
def calculate_antipode():
    print("yep")
    # user inputted address - Geocoding API
    # https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
    # address = "Amphitheatre+Parkway" #,+Mountain+View,+CA
    address = request.form['address']
    querystring = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={Maps_API_Key}"
    response = requests.get(querystring)
    json = response.json()


    # correct address to proper format
    # get coordinates of address
    coords = json['results'][0]['geometry']['location']
    latitude = coords['lat']
    longitude = coords['lng']

    # do math on coordinates to get antipode address/coordinates
    oppositeLat = -latitude
    oppositeLong = 180 - abs(longitude)
    if longitude > 0: oppositeLong = -oppositeLong
    
    # display antipode address/coordinates on maps
    zoom = 3
    endpoint = f"https://maps.googleapis.com/maps/api/staticmap?center={oppositeLat},{oppositeLong}&zoom={zoom}&size=400x400&key={Maps_API_Key}"
    #response = requests.post(endpoint)
    return render_template("index.html", MapRender=endpoint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
