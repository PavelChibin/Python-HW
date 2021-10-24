revenue = float(input("Введите значение выручки - "))
costs = float(input("Введите значение издержек - "))
result = revenue - costs
if result > 0:
    print(f"Отлично! Прибыль вашей компании  {result} !")
    print(f"Рентабильность выручки - {result / revenue:.3f}")
    persons = int(input("Сколько сотрудников работает в Вашей компании? - "))
    print(f"Прибыль на одного сотрудника составляет - {result / persons:.2f}")
elif result < 0:
    print(f"Компания работает с убытком - {-result}")
else:
    print(f"Компания отработала стабильно, в ноль")