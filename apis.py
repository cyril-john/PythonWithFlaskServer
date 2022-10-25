import requests

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
fullData = response.json()['items']
print( f"first print --> {fullData }")






