import requests
import json
import csv
import json
from gang_member import gang_member
from missing_person import missing_person
from base_person import base_person
import os
import asyncio

# Convert the following code to classes
# {'items': [{'subjects': [], 'title': "", 'aliases': [], 'details': ""}]}


async def fetch_fbi_wanted_list():
    while True:
        print("Fetching FBI wanted list...")
        response = requests.get("https://api.fbi.gov/wanted/v1/list")
        try:
            global value
            value = response.json()
            print("Fetched FBI wanted list")
        except json.decoder.JSONDecodeError as e:
            print("Error decoding JSON")
            # print(response.text)
            print(e)
            os.abort()
        await write_to_csv()
        await asyncio.sleep(60 * 60 * 24) # 24 hours

value: any = None


async def write_to_csv():

    ids = [item['uid'] for item in value['items']]
    names = [item['title'] for item in value['items']]
    subjects = [item['subjects'] for item in value['items']]
    aliases =  [item['aliases'] for item in value['items']]
    details =  [item['details'] for item in value['items']]


    with open('fbi-wanted_list.csv', mode='w') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['id', 'name', 'subjects', 'aliases', 'details'])
        
        # Write the data rows
        for id, name, subject, alias, detail in zip(ids, names, subjects, aliases, details):
            writer.writerow([id, name, subject, alias, detail])


def extract_first_last_name(full_name):
    names = full_name.split()
    return names[0], names[-1]


def show_menu() -> int:
    print("1. Show missing persons")
    print("2. Show gang members")
    print("3. Exit")
    return int(input("Enter your choice: "))


def show_gang_members():
    os.system("cls")
    people = get_people("Criminal Enterprise Investigations")
    gang_members = [convert_to_child(person, gang_member) for person in people]

    for i in range(len(gang_members)):
        print(f"[{i}] gang member: {gang_members[i].fornavn} {gang_members[i].efternavn} | gang name: {gang_members[i].gang_name}")

    choice = int(input("Enter the number of the person you want to select: "))

    print(f"gang member: {gang_members[choice].fornavn} {gang_members[choice].efternavn} | gang name: {gang_members[choice].gang_name}")
    gang_name = input(f"Enter the gang {gang_members[choice].fornavn} is a part of: ")
    gang_members[choice].gang_name = gang_name
    print("Saved!")
    main()

def show_missing_persons():
    os.system("cls")
    people = get_people("missing person")
    print(f"length of people: {len(people)}")
    missing_persons = [convert_to_child(person, missing_person) for person in people]
            
    for i, person in enumerate(missing_persons):
        print(f"[{i}] Missing person: {person.fornavn} {person.efternavn} | Last seen: {person.last_seen}")

    choice = int(input("Enter the number of the person you want to select: "))

    print(f"Selected missing person: {missing_persons[choice].fornavn} {missing_persons[choice].efternavn}")
    last_seen = input(f"Enter the last seen location of {missing_persons[choice].fornavn}: ")
    missing_persons[choice].last_seen = last_seen
    print("Saved!")
    main()


def get_people(subj: str) -> list[base_person]:
    persons: list[base_person] = []
    for values in value['items']:
        for subjects in values['subjects']:
            if subj.lower() not in subjects.lower():
                continue

            person = base_person()
            person.fornavn, person.efternavn = extract_first_last_name(values['title'])
            person.id = values['uid']
            persons.append(person)

    return persons


def convert_to_child(obj, valueType: type):
    value = valueType()
    value.id = obj.id
    value.fornavn = obj.fornavn
    value.efternavn = obj.efternavn
    return value

async def main():
    await fetch_fbi_wanted_list()


    choice = show_menu()
    if choice == 1:
        show_missing_persons()
    elif choice == 2:
        show_gang_members()
    elif choice == 3:
        print("Goodbye!")
        os.abort()
    else:
        os.system("cls")
        main()

if __name__ == "__main__":
    asyncio.run(main())