import urllib.request
import json

my_url = "http://0.0.0.0:8280/predict"

Square = 9.882643
LifeSquare = 33.432782
KitchenSquare = 6
Floor = 6
Ecology_1 = 0.310199
Social_1 = 11
Shops_1 = 0
HouseFloor = 14
HouseYear = 1972
BldId = 2304
DistrictId_count = 179
MedPriceByDistrict = 166809
MedPriceBySquare = None

body = {"Square": Square,
        "LifeSquare": LifeSquare,
        "KitchenSquare": KitchenSquare,
        "Floor": Floor,
        "Ecology_1": Ecology_1,
        "Social_1": Social_1,
        "Shops_1": Shops_1,
        "HouseFloor": HouseFloor,
        "HouseYear": HouseYear,
        "BldId": BldId,
        "DistrictId_count": DistrictId_count,
        "MedPriceByDistrict": MedPriceByDistrict,
        "MedPriceBySquare": MedPriceBySquare
        }

req = urllib.request.Request(my_url)
req.add_header('Content-Type', 'application/json; charset=utf-8')
json_data = json.dumps(body)
json_data_bytes = json_data.encode('utf-8')  # needs to be bytes
req.add_header('Content-Length', str(len(json_data_bytes)))
print(json_data_bytes)
response = urllib.request.urlopen(req, json_data_bytes)
js = json.loads(response.read())['predictions']
print(js)
