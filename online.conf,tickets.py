totalsum = 0
S = int(input("Введите количество билетов для покупки:\n"))
M = 1
print()
for amount in range(1, S + 1):

    print("Номер билета:", M)
    age = int(input("Введите возраст участника:"))
    price1 = 0
    price2 = 990
    price3 = 1390

    if age < 18:
        print("Стоимость билета:", price1, "рублей.")
    elif 18 <= age <=25:
        print("Стоимость билета:", price2, "рублей.")
        totalsum += price2
    else:
        print("Стоимость билета:", price3, "рублей.")
        totalsum += price3



    M = M+1
    print()

print("-----")
print()
print("Количество билетов:",  S)
print("Сумма к оплате:",totalsum)
if S > 3 and totalsum > 0:
    sum_with_discount = totalsum * 0.9
    print("Вам предоставлена скидка 10% за регистрацию более 3-х участников.\nСумма к оплате с учетом скидки:", sum_with_discount, "рублей.")
