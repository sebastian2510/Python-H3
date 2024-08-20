def main():
    name = input("What is your name? ")
    percentage_list = list()
    days = 3
    for i in range(days):
        day = 1
        percentage = int(input(f"Indtast % af færdiggjorte opgaver for dag {day}"))
        if (percentage < 0 or percentage > 100):
            print("Percentage must be between 0 and 100")
            days += 1
            continue
        day += 1
        percentage_list.append(percentage)
    


    
def get_score(percentage):
    if percentage == 100:
        return 12
    if percentage >= 90:
        return 10
    if percentage >= 70:
        return 7
    if percentage >= 50:
        return 4
    if percentage >= 20:
        return 2
    return 0