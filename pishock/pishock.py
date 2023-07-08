import requests
import json

url = "https://do.pishock.com/api/apioperate/"

# JSON payload
payload = {
    "Username": "Maikel1990",
    "Apikey": "a287bffc-fb32-488d-9d27-7591d58ed9c0",
    "Code": "value3"
    "Name": "Botje"
}

# Convert payload to JSON string
data = json.dumps(payload)

# Set headers
headers = {
    "Content-Type": "application/json"
}

# Send POST request
response = requests.post(url, headers=headers, data=data)

# Print response
print(response.text)
