import googlemaps
from datetime import datetime
import json
import io
from pprint import pprint

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

gmaps = googlemaps.Client(key='AIzaSyBTZa0fufi0LbRzGqlQcFBm8jop5HckCsk')

# Request directions

now = datetime.now()
directions_result = gmaps.directions("NW2 2LD",
                                     "BR1 5EG",
                                     waypoints = [
                                     "SM4 5BW",
                                     "SW11 8AZ",
                                     "SW18 3EL",
                                     "SW1W 8PG",
                                     "SW5 9JF"],
                                     mode="driving",
                                     departure_time = datetime.now(),
                                     optimize_waypoints = True)

with io.open('data.json','w', encoding='utf8') as outfile:
    str_ = json.dumps(directions_result, indent=4,
                        sort_keys=True,
                        separators=(',',': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

with open('data.json') as f:
    data = json.loads(f.read())

counter = 0

for a in data[0]['legs']:
    counter = counter + 1
    print("Stop: ",counter,";",
    "Destination: ",a['end_address'],";",
    "Distance: ",a['distance']['text'],";",
    "Duration: ",a['duration']['text'])
