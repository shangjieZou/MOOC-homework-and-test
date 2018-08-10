import datetime
import math

# This block is for bascketball prediction(Whether the team with higher score can win or not)
if (0):
    ch = ""
    while ch!= "q":
        HigherScores=int(raw_input("Scores higher:"))
        LeftSeconds = float(raw_input("Left Seconds: "))
        WhoIsControllingTheBall = raw_input("Is the team with higher score controlling the ball?(Yes or No):")
        ThreeScoresLower = HigherScores - 3
        RealScore = int()
        if ThreeScoresLower > 0:
            if WhoIsControllingTheBall=="Yes":
                RealScore = ThreeScoresLower + 0.5
            else:
                RealScore = ThreeScoresLower - 0.5
            if RealScore < 0:
                RealScore = 0
        else:
            RealScore = 0

        SquaredScore = RealScore**2
        if SquaredScore > LeftSeconds:
            print "Safe"
        else:
            print "Unsafe"
        ch = raw_input("Quit?")

if(0):
    #count = 0
    #for i in range(100,1000):
    #    if i%17==0:
    #        count += 1
    #print count

    max = 10
    sum = 0
    extra = 0

    for num in range(1, max):


        if num % 2 and not num % 3:
            sum += num
            print num
        else:
            extra += 1

    print sum


# Homework_T1
if(0):
    n = int(raw_input())
    sumNum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sumNum += i
    print sumNum


# Homework T2
if(0):
    n = int(raw_input())
    sumPrime = 0
    if n == 1:
        sumPrime = 0
    elif n == 2:
        sumPrime = 2
    else:
        for i in range(2, n):
            for k in range(2, int(math.sqrt(i)+1)):  # This int(math.sqrt(i)+1 can save time
                if i % k == 0:
                    break
            else:
                sumPrime += i
    print sumPrime


# Homework T3
if(0):
    # 1900 is not leap year, has 365 days
    # 1901 1.1 is Tuesday
    def DaysInMonth(Month, year):
        if Month==1 or Month==3 or Month==5 or Month==7 or Month==8 or Month==10 or Month==12:
            Days_In_Month = 31
        elif Month==4 or Month==6 or Month==9 or Month==11:
            Days_In_Month = 30
        else:
            if (year % 4 ==0 and year % 100 != 0) or year % 400==0:
                Days_In_Month = 29
            else:
                Days_In_Month = 28
        return Days_In_Month

    SumAllDay = 365-6
    SumSunday = 0
    for year in range(1901,2001):
        for Month in range(1,13):
            if (SumAllDay+DaysInMonth(Month,year)) % 7 == 0:
                SumSunday += 1
            SumAllDay += DaysInMonth(Month,year)
    print SumSunday


# Homework T4
if(0):
    n = int(raw_input())
    numberOfCirclePrimes = 0


    def primeOrNot(number):
        if number==2:
            prime = "Yes"
        elif number == 3:
            prime = "Yes"
        elif number>3:
            for i in range(2, number):
                for k in range(2, int(math.sqrt(i) + 1)):
                    if i % k == 0:
                        prime = "No"
                        break
                else:
                    prime = "Yes"
        return prime

    if n>10:
        numberOfCirclePrimes += 4
        for i in range(10,n):
            num_temp = i
            num_dontknowhowtosay = 0
            num_transfered = int
            while num_temp !=0:
                num_dontknowhowtosay = num_dontknowhowtosay*10 + num_temp % 10
                num_temp /= 10
                if num_dontknowhowtosay!=0:
                    num_transfered = int(str(num_dontknowhowtosay)+str(num_temp))
                    if primeOrNot(num_transfered) == "No":
                        break
                else:
                    numberOfCirclePrimes += 1
    elif n<= 10 and n>7:
        numberOfCirclePrimes = 4
    elif n>5 and n<=7:
        numberOfCirclePrimes = 3
    elif n>3 and n <=5:
        numberOfCirclePrimes = 2
    elif n==3:
        numberOfCirclePrimes = 1

    print numberOfCirclePrimes



n = int(raw_input())
numberOfCirclePrimes = 0
def primeOrNot(number):
    if number==2:
        prime = "Yes"
    elif number == 3:
        prime = "Yes"
    elif number>3:
        for i in range(2, number):
            for k in range(2, int(math.sqrt(i) + 1)):
                if i % k == 0:
                    prime = "No"
                    break
            else:
                prime = "Yes"
    return prime

if n>11:
    numberOfCirclePrimes = 4
    for i in range(10,n):
        num_temp = i
        num_dontknowhowtosay = 0
        num_transfered = int

        while num_temp !=0:
            num_dontknowhowtosay = num_dontknowhowtosay*10 + num_temp % 10
            num_temp /= 10
            num_newFirstNum = num_dontknowhowtosay * (10**len(str(i)))
            if num_dontknowhowtosay != 0:
                num_transfered = int(str(num_dontknowhowtosay)+str(num_temp))
                if primeOrNot(num_transfered) == "No":
                    break
                else:
                    print i
                    numberOfCirclePrimes += 1
elif n<= 10 and n>7:
    numberOfCirclePrimes = 4
elif n>5 and n<=7:
    numberOfCirclePrimes = 3
elif n>3 and n <=5:
    numberOfCirclePrimes = 2
elif n==3:
    numberOfCirclePrimes = 1
elif n==11:
    numberOfCirclePrimes = 4

print numberOfCirclePrimes
