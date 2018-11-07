A, B, C, D = 0, 0, 0, 0

while A <= 10:
    A += 2
    if A % 3 == 0:
        B += 1
    else:
        C += 1
    D += 1
print("A =", A)
print("B =", B)
print("C =", C)
print("D =", D)
