def numero_binomial():

    n = int(input("Determine o número de n: "))
    i = 0
    f = 1
    while i <= n and i != n:
        f = f * 1
        i = i + 1
        f = i * f
    print(f)      

    k = int(input("Determine o número de k: "))
    a = 0
    b = 1
    while a <= k and a != k:
        b = b * 1
        a = a + 1
        b = a * b
    print(b)

    print("O resultado é:", f // b * (f - b))

    

