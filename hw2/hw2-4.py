import sympy
import math
N = 5.0
dvc = 50.0
delta = 0.05
s3 = sympy.symbols("s3")
s4 = sympy.symbols("s4")
s1 = math.sqrt(8 / N * math.log(4 * math.pow(2 * N, dvc) / delta))
s2 = math.sqrt(2 / N * math.log(2 * N * math.pow(N, dvc))) + math.sqrt(2 / N * math.log(1 / delta)) + 1 / N
s3 = sympy.solve(s3 - sympy.sqrt(1 / N * (2 * s3 + sympy.log(6 / delta) + dvc * sympy.log(2 * N))), s3)
s4 = sympy.solve(s4 - sympy.sqrt(1 / (2 * N) * (4 * s4 * (1 + s4) + sympy.log(4 / delta) + dvc * sympy.log(N * N))), s4)
s5 = math.sqrt(16 / N * math.log(2 * math.pow(N, dvc) / math.sqrt(delta)))
print(s1, s2, s3[0], s4[0], s5)
