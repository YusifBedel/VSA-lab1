import math

x = 0.5
E = 0.001
P = 0.0
terim = x
n = 1

while abs(terim) > E:
    P += terim
    n += 1
    terim = ((-1) ** n) * (math.sin(x) ** (2 * n + 1)) / math.factorial(2 * n - 1)
            

print(f"P'nin yaxın dəyəri: {P}")
