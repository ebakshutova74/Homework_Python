def month_to_season(m):
    if m>2 and m<6:
        return 'Весна'
    elif m>5 and m<9:
        return 'Лето'
    elif m>8 and m<12:
        return 'Осень'
    else:
        return 'Зима'
m=input('Введите номер месяца: ')
print(month_to_season(int(m)))
