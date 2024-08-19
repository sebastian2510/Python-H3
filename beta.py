import requests
import json
import csv

# Convert the following code to classes
# {'items': [{'subjects': [], 'title': "", 'aliases': [], 'details': ""}]}

class FBIWantedItem:
    def __init__(self):
        self.subjects = []
        self.title = ""
        self.aliases = []
        self.details = ""

def fetch_fbi_wanted_list() -> list[FBIWantedItem]:
    response = requests.get("https://api.fbi.gov/wanted/v1/list")
    data: list[FBIWantedItem] = []
    resp = json.loads(response.text)

    # Foreach the items
    for item in resp['items']:
        fbi = FBIWantedItem()
        fbi.subjects = item['subjects']
        fbi.title = item['title']
        fbi.aliases = item['aliases']
        fbi.details = item['details']
        data.append(fbi)
    
    # Save the data to a .csv file
    with open("fbi_wanted.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title,", "Subjects,", "Aliases,", "Details,"])
        for fbi in data:
            writer.writerow([
                fbi.title,
                ", ".join(fbi.subjects), 
                ", ".join(fbi.aliases), 
                fbi.details
            ])

    return data

fetch_fbi_wanted_list()
    