def main():
    name = input("What is your name? ")
    percentage_list = list()
    days = 4
    day = 1
    for i in range(days):
        percentage = int(input(f"Indtast % af færdiggjorte opgaver for dag {day} "))
        if (percentage < 0 or percentage > 100):
            print("Percentage must be between 0 and 100")
            days += 1
            continue
        day += 1
        
        percentage_list.append(percentage)

    total_percentage = sum(percentage_list)
    score = total_percentage / 4
    print(f"Percentage: {score}% Total score: {get_score(score)}")
    


    
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

if __name__ == "__main__":
    main()