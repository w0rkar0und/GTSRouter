import googlemaps
from datetime import datetime
import json
import itertools
import responses


gmaps = googlemaps.Client(key='AIzaSyBTZa0fufi0LbRzGqlQcFBm8jop5HckCsk')

#Geocoding an address
#geocode_result = gmaps.geocode('11 Creighton Road, London, N17 8JU')

#print(geocode_result)

#Look up an address with reverse Geocoding
#reverse_geocode_result = gmaps.reverse_geocode((geocode_result))

#print(reverse_geocode_result)

#Request direction via car

#right_now = datetime.now()
responses.add(responses.GET,
                      'https://maps.googleapis.com/maps/api/directions/json',
                      body='{"status":"OK","routes":[]}',
                      status=200,
                      content_type='application/json')

routes = gmaps.directions("NW2 2LD","BR1 5EG",
                                        waypoints = ["SW17 9RH","SW8 3SU",
                                        "SE19 1BW","SE16 7EP","SW2 5QA",
                                        "SW19 6HA","SW19 2SS","SE6 2LA",
                                        "SW18 2BU"],
                                        mode="driving",
                                        departure_time = datetime.now(),
                                        optimize_waypoints = True)

beginning = "'legs': ["
ending = ", 'start_location':"

for x in routes:
    str_out = str(x)
#    print((str_out.split(beginning))[1].split(ending)[0])

print(str_out)

#print((str_out.split(beginning))[1].split(ending)[0])




#print(directions_result)

#results_in = json.dumps({'id':id})



#dumps_data = json.dumps(directions_result)

#print(type(directions_result),"directions_result")
#s = json.dumps(directions_result)
#a = json.loads(s)
#print(type(a))
#print(a)
#parsed_data = json.loads(dumps_data)
#print(type(parsed_data),"parsed_data")
#print(type(parsed_data),"parsed_data")
#print(type(dumps_data),"dumps_data")

#print(directions_result[0])
#print(parsed_data[0])

        #print(leg[0]['end_address'])
        #print(leg[0]['distance']['text'])
        #print(leg[0]['duration']['text'])
        #print (start, end, distance, duration)

#print (start, end, distance, duration)
