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


# Homework T4 Strategy 1: Example.1 Spent too long time. Example.2 consumed 94ms
if (0):
    import math
    n = int(raw_input())
    Count = 0

    def primeOrNot(number):
        prime = str
        if number==2:
            prime = "Yes"
        elif number == 3:
            prime = "Yes"
        elif number>3:
            for i in range(2, number+1):
                for k in range(2, int(math.sqrt(i) + 1)):
                    if i % k == 0:
                        prime = "No"
                        break
                else:
                    prime = "Yes"
        return prime


    for i in range(2, n):
        num_ForeheadNum = i
        num_BackNum = 0
        NewNum = i
        NumForLimitTheCycle = i
        while NumForLimitTheCycle != 0:
            num_BackNum = NewNum % 10
            num_ForeheadNum= NewNum / 10
            NewNum = num_BackNum * (10 ** (len(str(i))-1)) + num_ForeheadNum
            NumForLimitTheCycle /= 10
            if primeOrNot(NewNum) == "No":
                break
        else:
            Count += 1


# Homework T4 Strategy 2, Example.1 over time, Example.2 consumed 58ms
if(0):
    import math
    n = int(raw_input())
    Count = 0

    def primeOrNot(number):
        prime = str
        if number==2:
            prime = "Yes"
        elif number == 3:
            prime = "Yes"
        elif number>3:
            for i in range(2, number+1):
                for k in range(2, int(math.sqrt(i) + 1)):
                    if i % k == 0:
                        prime = "No"
                        break
                else:
                    prime = "Yes"
        return prime


    primeList = []
    for i in range(2, n):
        if primeOrNot(i) == "Yes":
            primeList.append(i)

    for SearchNum in range(0, len(primeList)):
        num_ForeheadNum = primeList[SearchNum]
        num_BackNum = 0
        NewNum = primeList[SearchNum]
        NumForLimitTheCycle = primeList[SearchNum]
        while NumForLimitTheCycle != 0:
            num_BackNum = NewNum % 10
            num_ForeheadNum= NewNum / 10
            NewNum = num_BackNum * (10 ** (len(str(primeList[SearchNum]))-1)) + num_ForeheadNum
            NumForLimitTheCycle /= 10
            if primeOrNot(NewNum) == "No":
                break
        else:
            Count += 1

    print Count


# Homework T4 Strategy 3, Example.1 over time, Example.2 consumed 65ms
if(0):
    import math
    n = int(raw_input())

    def primeOrNot(number):
        prime = str
        if number == 2:
            prime = "Yes"
        elif number == 3:
            prime = "Yes"
        elif number > 3:
            for i in range(2, number + 1):
                for k in range(2, int(math.sqrt(i) + 1)):
                    if i % k == 0:
                        prime = "No"
                        break
                else:
                    prime = "Yes"
        return prime


    primeList = []
    for i in range(2, n):
        if primeOrNot(i) == "Yes":
            primeList.append(i)

    CyclePrimeList = []
    print len(primeList)
    for SearchNum in range(0, len(primeList)):
        num_ForeheadNum = primeList[SearchNum]
        num_BackNum = 0
        NewNum = primeList[SearchNum]
        NumForLimitTheCycle = primeList[SearchNum]
        if (primeList[SearchNum] in CyclePrimeList) is False:
            while NumForLimitTheCycle != 0:
                num_BackNum = NewNum % 10
                num_ForeheadNum = NewNum / 10
                NewNum = num_BackNum * (10 ** (len(str(primeList[SearchNum])) - 1)) + num_ForeheadNum
                NumForLimitTheCycle /= 10
                if primeOrNot(NewNum) == "No":
                    break
            else:
                NumForLimitTheNextCycle = NewNum
                while NumForLimitTheNextCycle != 0:
                    num_BackNum = NewNum % 10
                    num_ForeheadNum = NewNum / 10
                    NewNum = num_BackNum * (10 ** (len(str(primeList[SearchNum])) - 1)) + num_ForeheadNum
                    NumForLimitTheNextCycle /= 10
                    if NewNum < n:
                        CyclePrimeList.append(NewNum)

    SettedList = list(set(CyclePrimeList))
    # CleanedList = []
    # for j in range(0, len(SettedList)):
    #    if SettedList[j] < n:
    #        CleanedList.append(SettedList[j])
    # print CleanedList
    print len(SettedList)





