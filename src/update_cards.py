import requests
import json

url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

# A GET request to the API
response = requests.get(url)

json_object = json.dumps(response.json(), indent=4)
print(json_object)
with open("data.json", "w") as outfile:
    outfile.write(json_object)