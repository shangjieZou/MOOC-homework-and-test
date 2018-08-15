import random


# Hanoi Tower:
if(0):
    def hanoi(n,A,B,C):
        if n == 1:
            print "Move", n, "from ", A,"to", C
        else:
            hanoi(n-1, A, C, B)
            print "Move", n ,"from", A, "to", C
            hanoi(n-1, B, A, C)

    hanoi(7,"Left", "Mid","Right")

# Convert to 2 JIn Zhi
if(0):
    def convert(n):
        if n == 0 or n == 1:
            return n
        else:
            return convert(n / 2) * 10 + n % 2

    print convert(9)

# Parking
if(0):
    def parking(low, high):
        if high - low < 1:
            return 0
        else:
            x = random.uniform(low, high-1)
            return parking(low, x) + 1 + parking(x+1, high)

    print parking(0, 5)

# Test
# T1
if(0):
    def foo():
        m = 1
        def bar():
             n = 2
             return m + n
        m = bar()
        print m
    foo()

if(0):
    def foo(arg1, arg2='test', arg3=100):
        print arg1, arg2, arg3
    foo(arg1 = 'where', arg2 = 'what')
    foo('where')
    foo('where', 'what')

if(0):
    def fib(n):
        f1, f2 = 0, 1
        while f2 < n:
            print f2,
            f1, f2 = f2, f1 + f2
    fib(10)

if(0):
    def gcd(m, n):
        r = m % n
        if r == 0:
            return n
        else:
            r = m % n
        return gcd(n, r)
    print gcd(15, 36)

# Homework T1
if(0):
    n = int(raw_input())
    def Fibonaci(i):
        a1 = 1
        a2 = 1
        an = 0
        if i == 1 or i == 2:
            return 1
        elif i > 2:
            for a in range(i-2):
                an = a1 + a2
                a1 = a2
                a2 = an
            return an

    def CountFibUnderNum(n):
        fib_list = []
        i = 1
        while Fibonaci(i) <= n:
            fib_list.append(Fibonaci(i))
            i += 1
        return fib_list

    def CountEvenFibUnderNum(n):
        list_EvenFib = []
        for i in range(len(CountFibUnderNum(n))):
            if CountFibUnderNum(n)[i] % 2 == 0:
                list_EvenFib.append(CountFibUnderNum(n)[i])
        return list_EvenFib


    print sum(CountEvenFibUnderNum(n))