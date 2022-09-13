import requests


endpoint1 = 'https://httpbin.org/status/200'
endpoint2 = 'https://httpbin.org/anything'
endpoint3 = 'http://localhost:8000/api/'

get_response = requests.get(endpoint3, json={"query":"Hello there!"}, params={'abc': 123} )


print(get_response.json())