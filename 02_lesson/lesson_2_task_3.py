import math
def square(side_sq):
        return (side_sq*side_sq)
    
side=input ('Введите размер стороны квадрата: ')
side_sq=math.ceil(float(side))
print ("Площадь квадрата равна " + str(square(side_sq)))
