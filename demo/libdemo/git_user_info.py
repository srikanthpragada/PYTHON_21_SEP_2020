import requests

user = "srikanthpragada"

resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code == 200:
    details = resp.json()
    print(details['company'])
    print(details['location'])
else:
    print(f"Sorry! {user} not found!")

