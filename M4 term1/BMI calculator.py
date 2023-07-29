
def bmi(a,b):
    
    x = weight/hight**2
    return x

weight = int(input('weight = '))
hight = int(input('Hight = '))

BMI = bmi(weight,hight)

if BMI < 18.5:
    print('ตำ่กว่าเกณฑ์')
elif BMI >= 18.5 & BMI <= 22.9:
    print('สมส่วน')
elif BMI >= 23 & BMI <= 24.9:
    print('นำ้หนักเกิน')
elif BMI >= 25 & BMI <= 29.9:
    print('โรคอ้วน')
else :
    print('โรคอ้วนอันตรายจะตายแล้ว')