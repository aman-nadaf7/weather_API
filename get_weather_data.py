import requests

cities =['Pune','Solapur','Patna']

API_KEY ="a1f5c4d341081aa8dbb75b3b5fd14fde"

for city_name in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        print("✅ Yes, we hit!")
        data = response.json()   # parse JSON response
        print(data)              # print full weather details
    else:
        print("❌ No, something went wrong")
        print(response.status_code, response.text)  # show error details
