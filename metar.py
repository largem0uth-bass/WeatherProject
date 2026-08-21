import requests

# Gets metar data from station passed into function
def get_metar(stationId, hoursBack):
    url = "https://aviationweather.gov/api/data/metar"

    # Dictionary of items to add to request

    payload = {
        "ids" : stationId,
        "format" : "json",
        "hours" : hoursBack
        }
    response = requests.get(url, params = payload)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

    

