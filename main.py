sum_tickets = 0
all_ticket = int(input("Введите количество билетов:"))
for age in range(all_ticket):
    age = int(input(f'Введите возраст участника:\n'))
    if age < 18:
        sum_tickets += 0
    elif 18 <= age and age <= 25:
        sum_tickets += 990
    elif age > 25:
        sum_tickets += 1390
if 3 <= all_ticket:
    sum_tickets *= 0.9
print("Общая стоимость билетов ровна:", sum_tickets)
