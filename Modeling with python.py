import matplotlib.pyplot as plt


# Logistic growth model----Chaos experiment
if(1):
    r = float(input("Set parameter r (Growth rate): "))
    a = 1+r
    x0 = float(input("Set the initial population: "))
    xm = float(input("Set the maximum limited of population:"))
    b = r/xm

    y = []
    iteration = []
    for i in range(200):
        if i == 0:
            y0 = b * x0/a
            y.append(y0)
            iteration.append(i)
        else:
            yi = a * y[i-1] * (1-y[i-1])
            y.append(yi)
            iteration.append(i)

    print (y)

    plt.plot(iteration, y)
    plt.title('Growth')
    plt.xlabel('Iterations')
    plt.ylabel('Y Sequence')
    plt.show()






