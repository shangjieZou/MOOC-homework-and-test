

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

    for num in range(1, max)


        if num % 2 and not num % 3:
            sum += num
            print num
        else:
            extra += 1

    print sum



