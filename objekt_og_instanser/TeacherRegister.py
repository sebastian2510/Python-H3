from FileManager import FileClass
from Teacher import teacher
from Company import TEC
import os
import time
import json

firm = FileClass.read_file()

courses = [
    "IoT embedded",
    "Python",
    "BigData 1",
    "Software sikkerhed og test",
    "Serverside programmering"
]


def register_teacher() -> None:
    os.system("cls")
    print("Opret lærer")
    name = input("Fornavn (tom for at gå tilbage): ")
    if name == "":
        return
    lastname = input("Efternavn (tom for at gå tilbage): ")
    if lastname == "":
        return
    
    if firm.find_teacher(name, lastname) is not None:
        print("Læreren eksisterer allerede!")
        input("Tryk enter tast for at gå tilbage")
        return
    
    new_teacher = teacher(name, lastname, [])
    add_course(new_teacher)


# Burde måske laves sammen med 
def select_teacher():
    if len(firm.teachers) == 0:
        print("Ingen lærere fundet!")
        time.sleep(3)
        return None
    for i, teacher in enumerate(firm.teachers):
        print(f"[{i}] {teacher.name} {teacher.lastname}")
    
    choice = int(input("Vælg lærer: "))
    if choice < 0 or choice > len(firm.teachers):
        print("Ugyldig værdi, prøv igen")
        return
    
    return firm.teachers[choice]

def update_teacher() -> None:
    os.system("cls")
    teacher = select_teacher()
    print("1. Tilføj fag")
    print("2. Fjern fag")
    choice = int(input("dit valg (tom for at gå tilbage): "))
    if choice is None:
        return
    
    if choice < 1 or choice > 2:
        print("Ugyldig valg!")
        time.sleep(3)
        return
    
    if choice == 1:
        add_course(teacher)
    else:
        remove_course(teacher)
    

def show_teachers():
    os.system("cls")
    if not firm.teachers or len(firm.teachers) == 0:
        print("Ingen lærere fundet!")
        time.sleep(3)
        return
    
    for teacher in firm.teachers:
        print(f"Lærer: {teacher.name} {teacher.lastname}")
        print("Fag:")
        for course in teacher.courses:
            print(f"- {course}")
    input("\nTryk enter tast for at gå tilbage ")



def remove_teacher():
    os.system("cls")
    teacher = select_teacher()
    firm.remove_teacher(teacher)
    FileClass.write_file(firm)


def remove_course(teacher: teacher):
    if teacher is None:
        print("Ingen lærer valgt!")
        time.sleep(3)
        return
    
    if teacher.courses is None or len(teacher.courses) == 0:
        print(f"{teacher.name} har ingen tildelte fag!")
        input("\nTryk enter tast for at gå tilbage")
        return

    
    for i, course in enumerate(teacher.courses):
        print(f"[{i}] {course}")
    
    choices = input("Vælg fag (seperaret med mellemrum, tom for at gå tilbage): ")
    if not choices:
        return
    
    if " " in choices:
        choices = list[int](int(choices.split()))
        for choice in choices:
            if choice < 0 or choice > len(courses):
                print(f"- ugyldig værdi: {choice}")
                continue
            teacher.courses.remove(teacher.courses[choice])
    else:
        choice = int(choices)
        if choice < 0 or choice > len(courses):
            print(f"- ugyldig værdi {choice}")
            return
        teacher.courses.remove(teacher.courses[choice])
    

def add_course(teacher):
    if teacher is None:
        print("Ingen lærer valgt!")
        time.sleep(3)
        return
    
    for i, course in enumerate(courses):
        print(f"- [{i}] {course}")

    # Get every choice seperated with a space
    choices = input("Vælg fag (seperaret med mellemrum for flere fag, tom for at gå tilbage): ")

    if not choices:
        return
    
    if " " in choices:
        choices = list[int](int(choices.split()))
        for choice in choices:
            if choice < 0 or choice > len(courses):
                print(f"- ugyldig værdi: {choice}")
                continue

            if courses[choice] in teacher.courses:
                print(f"Fag er allerede tildelt {teacher.name}: {courses[choice]}")
                continue
            teacher.courses.append(courses[choice])
    else:
        choice = int(choices)
        if choice < 0 or choice > len(courses):
            print(f"- ugyldig værdi {choice}")
            input("Tryk enter tast for at gå tilbage")
            return
        
        if courses[choice] in teacher.courses:
            print(f"Fag er allerede tildelt {teacher.name}: {courses[choice]}")
            input("Tryk enter tast for at gå tilbage")
            return
            
        teacher.courses.append(courses[choice])

    if len(teacher.courses) == 0:
        print("Ingen gyldige fag er tilføjet!")
        time.sleep(3)
        return

    print(f"Følgende fag er tilhørende {teacher.name}:")
    for course in teacher.courses:
        print(f"- {course}")

    firm.add_teacher(teacher)
    FileClass.write_file(firm)
    print("Gemt nyligt opdateret data!")
    time.sleep(3)

def save_and_exit():
    FileClass.write_file(firm)
    os.abort()

def show_menu() -> int:
    while True:
        os.system("cls")
        print("1. Opret lærer")
        print("2. Opdater lærer")
        print("3. Vis liste af lærere")
        print("4. Fjern lærer")
        print("5. Save & Exit")
        choice = int(input("dit valg: ").strip())
        if choice < 1 or choice > 5:
            continue
        
        if choice == 1:
            register_teacher()
        elif choice == 2:
            update_teacher()
        elif choice == 3:
            show_teachers()
        elif choice == 4:
            remove_teacher()
        elif choice == 5:
            save_and_exit()

show_menu()