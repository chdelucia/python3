def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power   ## como un return pero sin romper la serie
        power *= 2


for v in powers_of_2(8):
    print(v)


# Recommended:
def f(x): return 3*x


# Not recommended:
f = lambda x: 3*x