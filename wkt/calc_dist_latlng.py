from geopy.distance import vincenty

coords_1 = (37.41700482527499, -122.14679083380338 )
coords_2 = (37.417010630455636, -122.14679196722622 )

print vincenty(coords_1, coords_2).m 
