# importing the requests library
import requests
import untangle

# api-endpoint
URL = "https://maps.googleapis.com/maps/api/directions/xml"

# origin given here
origin = "NW2 2LD"
destination = "BR1 5EG"
key = "AIzaSyBTZa0fufi0LbRzGqlQcFBm8jop5HckCsk"
waypoints = "SW8 3SU|SW18 2BU|SE6 2LA"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'origin':origin, 'destination':destination, 'key':key, 'waypoints':waypoints}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

print(r)
# extracting data in json format
#data = untangle.parse(r)

#for key in data:
#    print(len(key))

#print(type(data))

#print(data[geocoded_waypoints])
#print(data)
