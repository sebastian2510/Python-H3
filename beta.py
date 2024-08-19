import requests
import json
import csv
from gang_member import gang_member
from missing_person import missing_person
from base_person import base_person
import os

# Convert the following code to classes
# {'items': [{'subjects': [], 'title': "", 'aliases': [], 'details': ""}]}

def fetch_fbi_wanted_list():
    response = requests.get("https://api.fbi.gov/wanted/v1/list")
    return response.json()

value = fetch_fbi_wanted_list()
titles = [item['title'] for item in value['items']]
subjects = [item['subjects'] for item in value['items']]
aliases = [item['aliases'] for item in value['items']]
details = [item['details'] for item in value['items']]

def write_to_csv():
    with open('fbi_wanted_list.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Subjects', 'Aliases', 'Details'])
        for i in range(len(titles)):
            writer.writerow([titles[i], subjects[i], aliases[i], details[i]])

write_to_csv()

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
    gang_members = [person for person in people if isinstance(person, gang_member)]

    for i in range(len(gang_members)):
        print(f"[{i}] gang member: {gang_members[i].fornavn} {gang_members[i].efternavn} | gang name: {gang_members[i].gang_name}")

    choice = int(input("Enter the number of the person you want to select: "))

    print(f"gang member: {gang_members[choice].fornavn} {gang_members[choice].efternavn} | gang name: {gang_members[choice].gang_name}")
    gang_name = input(f"Enter the gang {gang_members[choice].fornavn} is a part of: ")
    gang_members[choice].gang_name = gang_name
    print("Saved!")
    show_menu()

def show_missing_persons():
    os.system("cls")
    people = get_people("missing person")
    print(f"length of people: {len(people)}")
    missing_persons = [person for person in people if isinstance(person, missing_person)]
            
    for i, person in enumerate(missing_persons):
        print(f"[{i}] Missing person: {person.fornavn} {person.efternavn} | Last seen: {person.last_seen}")

    choice = int(input("Enter the number of the person you want to select: "))

    print(f"Selected missing person: {missing_persons[choice].fornavn} {missing_persons[choice].efternavn}")
    last_seen = input(f"Enter the last seen location of {missing_persons[choice].fornavn}: ")
    missing_persons[choice].last_seen = last_seen
    print("Saved!")
    show_menu()


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

def main():

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

main()