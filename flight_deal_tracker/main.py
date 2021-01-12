# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
# from flight_data import FlightData

index = 1
data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_data()

# Update google-sheet with the IATA codes
for data in sheet_data["prices"]:
    index += 1
    if data["iataCode"] == "":
        print("In")
        place_name = data["city"]
        iata_code = flight_search.get_iata_code(place_name)
        data["iataCode"] = iata_code
        data_manager.update_iatacode(data, index)

print(flight_search.get_data("PAR"))

