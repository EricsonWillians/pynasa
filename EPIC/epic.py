import argparse
import requests
import json

class Epic:

    EPIC_URL = "https://epic.gsfc.nasa.gov/api/natural"

    def __init__(self):
        self.json_data = self.fetchData()

    def fetchData(self):
        response = requests.get(self.EPIC_URL)
        json_data = json.loads(response.text)
        return json_data

    def getDates(self):
        dates = []
        for data in self.json_data:
            date = data["date"].split(' ')[0].replace('-', '')
            if not (date in dates):
                dates.append(date)
        return dates

    def printData(self):
        print(json.dumps(self.fetchData(), indent=4, sort_keys=True))

if __name__ == "__main__":
    epic = Epic()
    print(epic.getDates())
    # epic.printData()