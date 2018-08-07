import math
import datetime

if(0):
    pi = 3.14
    radius = float(raw_input("Radius:"))
    area = pi*radius**2
    print area


if(0):
    a = 10
    b = 40
    c = 15
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    test = math.sqrt(b**2-4*a*c)
    print str(x1)+" "+str(x2)
    print a*x1*x1+b*x1+c
    print a * x2 * x2 + b * x2 + c

if(0):
    TotalMoney = 0
    for i in range(1,11):
        TotalMoney = (TotalMoney + 1000) * (1+0.047)
        i += 1
    print TotalMoney

if(0):
    print datetime.date.today()


if(0):
    Weight = float(raw_input("Weight:"))
    Height = float(raw_input("High: "))
    BMI = Weight/(Height**2)
    print ("{:.2f}".format(BMI))

if(0):
    Second = float(raw_input())
    Hour = Second // 3600
    minute = (Second % 3600) // 60
    Sec = Second-(Hour*3600)-(minute*60)
    print str(int(Hour))+" "+str(int(minute))+" "+str(int(Sec))

if(0):
    import math
    a = float(raw_input())
    b = float(raw_input())
    c = float(raw_input())
    cosC = -1*(c**2-a**2-b**2)/(2*a*b)
    print ("{:.1f}".format(math.degrees(math.acos(cosC))))
