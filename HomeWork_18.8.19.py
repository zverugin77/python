print("\nВЫ РЕГИСТРИРУЕТЕСЬ НА ОНЛАЙН-КОНФЕРЕНЦИЮ: \n")
all_price = 0
ticket = int(input('Солько Вам нужно билетов? Введите количесвто: '))
for i in range(ticket):
    i += 1
    age_for_ticket = int(input(f'Введите цифрами возраст для {i} билета: '))
    if age_for_ticket < 18:
            print('Билет для несовершеннолетних бесплатный !!!')
    elif 18 <= age_for_ticket < 25:
            all_price += 990
            print('Стоимость билета лицам от 18 до 25 лет - 990 руб.')
    else:
            all_price += 1390
            print('Стоимость билета лицам от 25 лет - 1390 руб.')

if ticket > 3:
    print('Вы купили свыше 3-х билетов и Вам положена скидка !!!')
    all_price = all_price - ((all_price / 100) * 10)
    print(f'Сумма к оплате - {all_price} руб. (с учетом скидки 10%, т.к. Вы зарегистрировали больше 3-х человек)!')
else:
    print(f'Сумма к оплате - {all_price} руб.')