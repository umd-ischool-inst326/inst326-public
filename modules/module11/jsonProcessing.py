import requests
import json

jsonFile = requests.get("http://www.cs.umd.edu/~golbeck/example.json")
jsonObject = json.loads(jsonFile.content)

print (jsonObject["person"]["name"])