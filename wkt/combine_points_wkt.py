#  This scripts merges multiple wkt points into one multipoint

import sys
import os
import re

# parses wkt("POINT(lng, lat)") to lng, lat
def parse_wkt(wkt):
   latlngalt_str = str(re.findall(r"\(([^()]+)\)", str(wkt))) # extract from inside []      
   
   lng = re.findall("([-.0-9]*)", latlngalt_str.split(" ")[0])[2] # removes ['
   lat = re.findall("([-.0-9]*)", latlngalt_str.split(" ")[1])[0]
   
   return float(lng), float(lat)

output_filename = sys.argv[2]
f_out=open(output_filename, 'w')
f_out.write("MULTIPOINT(")

list_latlngs = []

filepath = sys.argv[1]

with open(filepath, 'r') as f:
    lines = f.readlines()
    for line in lines:
       lng_f, lat_f = parse_wkt(line)
       f_out.write(str(lng_f) + " "+str(lat_f)+",")

f_out.write(")")
