import requests
import json

print('Hello World')
response = requests.get("https://itsthisforthat.com/api.php?json")
response = json.loads(response.text)
print(f"Basically it's a {response['this']} for {response['that']}")