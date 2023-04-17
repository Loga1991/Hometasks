tickets = int(input("Введите количество билетов: "))

spisok = []

N = tickets

for people in range(1, N + 1):
    age = int(input("Введите возраст: "))
    if age < 18:
        price = 0
        print ("Бесплатно")
    elif 18 <=age <=25:
        price = 990
        print ("Цена: 990 ")
    elif age > 25:
        price = 1390
        print("Цена: 1390 ")
    spisok.append(price)

total = sum(spisok)
if N > 3:
    discount = total - (total/10)
    print ("Итого: ", discount)
else:
    print ("Итого: ", total)