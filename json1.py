"""import json

people = {
    "is_active" : False,
    "1": None,
    "hi": 32
"""


#print(json.loads(peopel))




"""
with open("fayl.json", "w" ) as f:
    print(json.dump(people,f))


with open("fayl.json", "w" ) as f:
    print(json.load(f))
"""
#import json
"""
import requests
from pprint import pprint
response = requests.get("https://api.soff.uz/api/v1/customer/documents/")
#print(response.status_code)

if response.status_code == 200:
    data = response.json()
#    pprint(data)
im = []
for i in data['results']:
    im.append(i['poster_url'])

    """







# homework 1

#  json >>> python

"""
import json

people = {

    "aziz":"leader",
    "diyor": "creator",
    "john":"admin",
    "shox": false
}


print(json.loads(people))

"""

# homework 2

# pythpn >>> json
"""import json
people = {

    "aziz":"leader",
    "diyor": "creator",
    "john":None,
    "shox": False
}

print(json.dumps(people))"""

# homework 3

"""import json
people = {

    "aziz":"leader",
    "diyor": "creator",
    "john":None,
    "shox": False
}

print(json.dumps(people, indent=4))



"""


#------------------------------------------------------------------------------- 
# {}fayl.json >>> python

"""import json

with open ("fayl.json", "r") as f :
    print(json.load(f))
"""

#--------------------------------------------------------------------------------
#python >>> {}fayl.json


"""import json
people = {

    "aziz":"leader",
    "diyor": "creator",
    "john":None,
    "shox": False
}
with open ("fayl.json", "w+") as f :
    print(json.dump(people,f, indent=4))
"""




# hoemmwork 3,4


"""import json
import requests
from pprint import pprint

respose = requests.get("https://api.soff.uz/api/v1/customer/documents/")
if respose.status_code == 200:
    date = respose.json()


narx = []
for i in date["results"]:
    narx.append(i["price"])

pprint(narx)"""

"""
import json
from pprint import pprint

with open ('fayl.json', "r") as f :
    data  = json.load(f)
    for i in data:
        print(i['name']['common'],i["area"])



"""




# import json

# with open("fayl.json","r") as f:
    





















































































































































































































