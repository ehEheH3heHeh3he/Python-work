import math

type = input('c=circle\nt=triangle\nr=rectangle\ns=sphere\n\nenter : ')

def sphere(r):
    V= 4.0/3.0*math.pi* r**3
    return V
def circle(r2):
    V = math.pi *r2 *r2
    return V
def triangle(base,hight):
    V = base*hight*0.5
    return V
def rectangle(widthh,length):
    V = widthh*length
    return V

if type == 's' :
    r = int(input('enter radius : '))
    volume = sphere(r)
    print('The volume of the sphere is: ',volume)
elif type == 'c' :
    r2 = int(input('enter radius : '))
    area_c = circle(r2)
    print('The area of the circle is: ',area_c)
elif type == 't' :
    base = int(input('enter base : '))
    hight = int(input('enter hight : '))
    area_t = triangle(base,hight)
    print('The area of the triangle is: ',area_t)
elif type == 'r' :
    widthh = int(input('enter width : '))
    length = int(input('enter length : '))
    area_r = rectangle(widthh,length)
    print('The area of the regtangle is: ',area_r)
else :
    print('error u moron')






