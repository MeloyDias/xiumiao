# importing the requests library 
import requests 
  
# api-endpoint 
URL = "https://public-api.tracker.gg/apex/v1/standard/profile/5/MeloyDias"
HDR = {"TRN-Api-Key": "13a5baf3-d482-4fec-8e50-95aec6444739"}  
# sending get request and saving the response as response object 
r = requests.get(url=URL, headers=HDR) 
  
# extracting data in json format 
j = r.json() 

# Get Stats
Level     = j['data']['stats'][0]['value']
Kills     = j['data']['stats'][1]['value']
Headshots = j['data']['stats'][2]['value']

print(f"MeloyDias, Level {Level} has {Kills} kills and {Headshots} headshots.")
