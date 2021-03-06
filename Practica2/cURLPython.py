import requests

url = "https://pokemon-go1.p.rapidapi.com/pokemon_stats.json"

headers = {
    'x-rapidapi-key': "35c1f9d0damsh247d3b0d55183e6p18f615jsn3a0339f4b9f2",
    'x-rapidapi-host': "pokemon-go1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)


print(response.text)


url = "https://pokemon-go1.p.rapidapi.com/pokemon_rarity.json"

headers = {
    'x-rapidapi-key': "35c1f9d0damsh247d3b0d55183e6p18f615jsn3a0339f4b9f2",
    'x-rapidapi-host': "pokemon-go1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
