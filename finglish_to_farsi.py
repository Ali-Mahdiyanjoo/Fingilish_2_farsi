import requests
import json

url = "https://9mkhzfaym3.execute-api.us-east-1.amazonaws.com/production/convert?"
payload = input("in ja ye chizi benevis? ")
headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
  'Accept-Language': 'en-US,en;q=0.5',
  'Content-Type': 'text/plain'
}
response = requests.request("POST", url, headers=headers, data=payload)
json_data = json.loads(response.text)
values = json_data.values()
print(values)