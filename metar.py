import requests
import json
from config import METAR_FIELDS
# Gets metar data from station passed into function
def getMetar(stationId, hoursBack=0, format="json"):
    url = "https://aviationweather.gov/api/data/metar"

    # Dictionary of items to add to request

    payload = {
        "ids" : stationId,
        "format" : format,
        "hours" : hoursBack
        }
    response = requests.get(url, params = payload)
    
    if response.status_code == 200:
        data = response.json()
        return data[0]
    else:
        return None

# Creates a formatted string of raw metar data
def dumpsMetar(data):
    return json.dumps(data, indent=4)

# Build dictionary of wanted datapoints
def formatMetar(data):
    formattedData = {}
    for field in METAR_FIELDS:
        formattedData[field] = data.get(field)
    return formattedData






    

