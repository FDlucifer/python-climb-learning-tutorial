# python3
# pip install geocoder
# pip install geopy

from geopy.geocoders import Nominatim
from geopy import distance, location
from geopy.point import _normalize_coordinates

geocoder = Nominatim(user_agent="lUc1f3r11")
location1 = "beijing"
location2 = "shanghai"

coordinates1 = geocoder.geocode(location1)
coordinates2 = geocoder.geocode(location2)

lat1, long1 = (coordinates1.latitude), (coordinates1.longitude)
lat2, long2 = (coordinates2.latitude), (coordinates2.longitude)

place1 = (lat1, long1)
place2 = (lat2, long2)

print(coordinates1)
print(coordinates2)
print(f"The Distance Between {location1} and {location2} Is:", distance.distance(place1, place2))