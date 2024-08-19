import requests
import json

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
    for item in resp['items']:
        fbi = FBIWantedItem()
        fbi.subjects = item['subjects']
        fbi.title = item['title']
        fbi.aliases = item['aliases']
        fbi.details = item['details']
        data.append(fbi)

    return data
    
test = fetch_fbi_wanted_list()
print(test)

