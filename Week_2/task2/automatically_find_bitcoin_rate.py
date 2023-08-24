import requests
import os

req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# save data into a txt file
location = os.path.dirname(os.path.realpath(__file__))

#if file is not generated, generate it in this location
os.chdir(location)

if os.path.isfile(location+"/data.txt") == False:
    fd = open("data.txt","x")
else:
    fd = open("data.txt","w")
    
# always overwrite file data
fd.seek(0)

data = req.json()

for currency in data["bpi"]:
    fd.write(f"info about {currency}:\n")
    for info in data["bpi"][currency]:
        fd.write(f'{info} : {data["bpi"][currency][info]}\n')
    fd.write("\n")    

