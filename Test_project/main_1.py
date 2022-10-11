import requests

response = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 531,
  "category": {
    "id": 926,
    "name": "string"
  },
  "name": "rio",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)


response = requests.put("https://petstore.swagger.io/v2/pet", json={
  "id": 531,
  "category": {
    "id": 926,
    "name": "string"
  },
  "name": "LOLO",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)


response = requests.get('https://petstore.swagger.io/v2/pet/531')
print(response.text)
