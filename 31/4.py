from math import pow

def compound_interest(P, R, T, n):
    A = P * pow((1 + R / n), n * T)
    CI = A - P
    return CI

result = compound_interest(1000, 0.05, 2, 4)
print("Compound interest is:", result)