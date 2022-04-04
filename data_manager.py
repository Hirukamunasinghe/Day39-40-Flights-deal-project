import requests
SHEETY_ENDPOINT = "https://api.sheety.co/5d5da77f21a37c34e9c61491334073e4/flightDeals1/prices"

class DataManager:
    def __init__(self):
        self.destination_data ={}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data={
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}",json=new_data)
            #print(response.text)
