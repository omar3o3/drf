import requests

endpoint = 'http://localhost:8000/api/'

# get_response = requests.get(endpoint)
# print(get_response.text)
# print(get_response.json()['message'])
# print(get_response.status_code)
# print(get_response)

# get_response = requests.get(endpoint, params={'abc': 123}, json={'query': "Hello world!"})
get_response = requests.post(endpoint, json={'title': 'Hello world'})


print(get_response.json())