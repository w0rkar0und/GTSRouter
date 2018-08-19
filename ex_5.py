import googlemaps
from datetime import datetime, timedelta
import time
import json
import io
from pprint import pprint
import pandas as pd
#from pandas import ExcelWriter
#from pandas import ExcelFile

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

vias = []

depot = input("Enter Start Postcode: ")
home = input("Enter End Postcode: ")

# User to select File or Manual Post Code upload

method = input("File (F) or Manual (M)?")

# if Manual input, build vias list from the input, else user inputs the file
# name and vias is built using the file contents -  in column Postcode

if method.lower() == "m":
    for i in range(0,23):
        entry = input("Enter Postcode: ")
        if entry.lower() == "exit":
            break
        else:
            vias.append(str(entry))
elif method.lower() == "f":
    file = input("Enter Filename:") + ".xlsx"
    df = pd.read_excel(file,sheet_name=0)
    vias = df['Postcode'].tolist()

# Google Maps API client key
start_time = time.time()
gmaps = googlemaps.Client(key='AIzaSyBTZa0fufi0LbRzGqlQcFBm8jop5HckCsk')

# Request directions from Google Maps Directions API

now = datetime.now()
directions_result = gmaps.directions(depot,
                                     home,
                                     waypoints = vias,
#                                     [
#                                     "SM4 5BW",
#                                     "SW11 8AZ",
#                                     "SW18 3EL",
#                                     "SW1W 8PG",
#                                     "SW5 9JF"],
                                     mode="driving",
                                     departure_time = datetime.now(),
                                     optimize_waypoints = True)

# Write output as JSON file

with io.open('data.json','w', encoding='utf8') as outfile:
    str_ = json.dumps(directions_result, indent=4,
                        sort_keys=True,
                        separators=(',',': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Read JSON output from Google API request

print("")
print("*********** OPTIMISED ROUTE ***********")
print("")
print("Origin-----------:",depot.upper())
print("")
print("Destination------:",home.upper())
print("")
print("Date/Time of Run-:",datetime.now().ctime())
print("")

with open('data.json') as f:
    data = json.loads(f.read())
    f.close()

counter = 0
total_time = 0
total_distance = 0
rpt = "report.txt"
txt = "route.txt"

f = open(rpt,'w')
f.write("\n")
f.write("*********** OPTIMISED ROUTE ***********\n")
f.write("\n")
f.write("Origin-----------: "+depot.upper()+"\n")
f.write("\n")
f.write("Destination------: "+home.upper()+"\n")
f.write("\n")
f.write("Date/Time of Run-: "+datetime.now().ctime()+"\n")
f.write("\n")

r = open(txt,'w')

r.write(datetime.now().ctime()+"\n")
r.write("\n")
r.write(depot.upper()+"\n")
r.write("\n")


# Print the optimised route, by Stop/Destination/Distance/Time

for a in data[0]['legs']:
    counter = counter + 1
    end_add = a['end_address']
#    tt = a['duration']['value'] / 3600
    time_to = timedelta(seconds=a['duration']['value'])
    total_time = total_time + a['duration']['value']
    td = a['distance']['value'] * 0.000621371192
    total_distance = total_distance + td
#    print("Stop: ",counter,";",
#    "Destination: ",a['end_address'],";",
#    "Distance: ", round(td,2),"miles",";",
#    "Duration: ", round(tt,2),"hours")
    print_str = "|Stop: {0:<2} "\
                "|Add: {1:<65} "\
                "|Dist: {2:<5} miles   |"\
                "Time: {3} hh:mm:ss|"
    print(print_str.format(counter,end_add,round(td,2),time_to))
    f.write(print_str.format(counter,end_add,round(td,2),time_to)+"\n")
    r.write(str(counter)+": "+str(end_add)+"\n")

print("")
print("Total Time:",timedelta(seconds=total_time),"hh:mm:ss")
print("Total Distance:",round(total_distance,2),"miles")
print("***************************************")
print("Runtime: %s seconds ---" % (time.time() - start_time))

f.write("\n")
f.write("Total Time: "+str(timedelta(seconds=total_time))+" hh:mm:ss\n")
f.write("Total Distance: "+str(round(total_distance,2))+" miles\n")
f.write("***************************************\n")
f.write("Runtime: %s seconds ---\n" % (time.time() - start_time))

f.close()

r.write("\n")
r.write(home.upper()+"\n")
