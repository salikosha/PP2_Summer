print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")

import json


with open('/Users/saliko/Desktop/PP2_Summer/Practice4/JSON/sample.json', 'r') as file:
    data = json.load(file)

for obj in data['imdata']:
    print(obj['l1PhysIf']['attributes']['dn'], "                              inherit   9150 ")

    
    