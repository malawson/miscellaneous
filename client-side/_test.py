import requests 
import json 

"""
r = requests.get("http://www.python.org/")

with open("python_org.html", "wb") as code:
	code.write(r.content)

"""

url = 'http://httpbin.org/post'
payload = {"colors":[

		{"color": "red", "hex": "#f00"},
		{"color": "green", "hex": "#0f0"},
		{"color": "blue", "hex": "#00f"},		
		{"color": "cyan", "hex": "#0ff"},
		{"color": "yellow", "hex": "#ff0"},
		{"color": "black", "hex": "#000"},
		{"color": "magenta", "hex": "#f0f"},
		]}

headers = {"content-type": "application/json"}

# POST request 
response = requests.post(url, data=json.dumps(payload), headers=headers)

# output response

print response.status_code


