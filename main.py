import requests
import json

url = "http://tsk-mosenergo.1sim.online:81"
url_to_get_token = f"{url}/api2/auth/open"
url_to_get_companies = f"{url}/api2/company"
url_to_get_values = f"{url}/api2/values"

payload = {
  "login": "a.ryadinskih@tsk-mosenergo.ru",
  "password": "Sfrffccc2511"
}

response = requests.post(url=url_to_get_token, params=payload)

token = response.json()["token"]
print(token)

headers = {
    "Authorization": f"Bearer {token}",
}


with open('request.txt', "r") as file:
    payload = file.read()


response = requests.get(url_to_get_values, headers=headers, data=payload)

print(json.dumps(response.json()[2], ensure_ascii=False, sort_keys=True, indent=2))

with open('response.txt', 'w') as file:
    json.dump(response.json(), file, ensure_ascii=False, sort_keys=True, indent=2)

T1 = response.json()[2]["val"]
print(T1)