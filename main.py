from math import factorial

def generate_sequence_a(x):
    k = 0
    while True:
        yield (x ** (2 * k)) / factorial(2 * k)
        k += 1

def product_sequence_b(n):
    result = 1
    for k in range(1, n + 1):
        result *= (1 + 1 / (k ** 2))
    return result

def determinant_sequence_c(a, b, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    return a * determinant_sequence_c(a, b, n - 1) + b * determinant_sequence_c(a, b, n - 2)

def sum_sequence_d(n):
    a1, a2 = 1, 1
    total = a1 + a2
    for _ in range(3, n + 1):
        a1, a2 = a2, a1 + a2
        total += a2
    return total if n > 2 else 1

def taylor_approximation_e(x, epsilon=1e-6):
    k = 1
    term = k * x ** (k - 1)
    total = 0
    while abs(term) > epsilon:
        total += term
        k += 1
        term = k * x ** (k - 1)
    return total


print("8.3.5. a) Перші 6 елементів послідовності при x = 2:")
gen_a = generate_sequence_a(2)
for _ in range(6):
    print(f"{next(gen_a):.5f}", end=' ')
print("\n")

print("8.3.5. b) Добуток P_n при n = 5:")
print(f"{product_sequence_b(5):.5f}\n")

print("8.3.5. c) Визначник порядку n = 5 при a = 2, b = 3:")
print(determinant_sequence_c(2, 3, 5), "\n")

print("8.3.5. d) Сума перших 10 елементів послідовності:")
print(sum_sequence_d(10), "\n")

print("8.3.5. e) Тейлорівське наближення при x = 0.5, ε = 1e-6:")
print(f"{taylor_approximation_e(0.5):.5f}")