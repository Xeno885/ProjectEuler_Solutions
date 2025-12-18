def sum_multiples(k, target):
    n = (target - 1) // k
    return k * (n * (n + 1)) // 2

target = 1000
result = sum_multiples(3, target) + sum_multiples(5, target) - sum_multiples(15, target)

print(result)
