def generate_fibonacci(limit):
    fib_sequence = []
    a, b = 0, 1
    while a < limit:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
limit_value = 4000000
fib_numbers = generate_fibonacci(limit_value)
sum = 0
for i in fib_numbers:
    if i%2 == 0:
        sum = sum + i
    else:
        pass
print(sum)
