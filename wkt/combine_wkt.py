combine_wkt.py

Type
Text
Size
2 KB (1,814 bytes)
Storage used
2 KB (1,814 bytes)
Location
My Drive
Owner
me
Modified
Oct 24, 2018 by me
Opened
5:33 PM by me
Created
Oct 24, 2018 with Google Drive Web
Add a description
Viewers can download
#  This scripts merges multiple wkt into one
#  Assuming each file only has one wkt
#  python combine_wkt.py input_dir output_file
#  Only writing points based on height (thres_height_m to max_height_m)
#  Also clusters latlngs likely from the same traffic element

import sys
import os
import re
import numpy as np
from sklearn import cluster

geoid = -32.05 # HAE - Geoid = MSL
ground_height = 17

min_height_from_ground = 5.2 # approximate length in meters of traffic lights
thres_height_m = ground_height + min_height_from_ground
max_height_m = ground_height + 2.5 * min_height_from_ground

# parses wkt(MULTIPOINT[lng, lat, alt]) to lng, lat, alt
def parse_wkt(wkt):
   latlngalt_str = str(re.findall(r"\(([^()]+)\)", str(wkt))) # extract from inside []      
   
   lng = re.findall("([-.0-9]*)", latlngalt_str.split(" ")[0])[2] # removes ['
   lat = latlngalt_str.split(" ")[1]
   alt = re.findall("([-.0-9]*)", latlngalt_str.split(" ")[2])[0]
   
   return float(lng), float(lat), float(alt)


input_dir = sys.argv[1]
file_list = os.listdir(input_dir)
num_files = len(file_list)

output_filename = sys.argv[2]
f_out=open(output_filename, 'w')
f_out.write("MULTIPOINT(")

list_latlngs = []

for filename in file_list:
   filepath = os.path.join(input_dir, filename)

   with open(filepath, 'r') as f:
       wkt = f.readline()
       lng_f, lat_f, alt_f = parse_wkt(wkt)
       alt_f = alt_f - Geoid

      # if (alt_f > thres_height_m and alt_f < max_height_m):
       list_latlngs.append([lng_f, lat_f])

latlngs = np.array(list_latlngs)
num_clusters = 12
kmeans = cluster.KMeans(n_clusters=num_clusters, random_state=0).fit(latlngs)

print kmeans.inertia_

for x in xrange(num_clusters):
   f_out.write(str(kmeans.cluster_centers_[x, 0]) + " "+str(kmeans.cluster_centers_[x, 1]) + ",")

f_out.write(")")
