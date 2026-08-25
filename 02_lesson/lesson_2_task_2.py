def is_year_leap (year):
    if year_result % 4 == 0:
        return True
    else:
        return False
      
year=input("Введите год в формате ГГГГ: ")

year_result=int(year)


print('Год ' + str(year_result) + ' : ' + str(is_year_leap(year_result)))
