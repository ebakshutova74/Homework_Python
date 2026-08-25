def fizz_buzz(n):
    if n % 3 ==0 and n % 5 ==0:
        return('FizzBuzz')
    elif n % 5 ==0:
        return('Buzz')
    elif n % 3 ==0 :
        return('Fizz')
    else:
        return(n)
    
s=input('Введите целое число: ')
n=int(s)
for n in range(1, n+1):
    print(fizz_buzz(n))
