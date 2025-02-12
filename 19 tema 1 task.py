def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def filtruoti_lyginius(seka):
    for skaicius in seka:
        if skaicius % 2 == 0:
            yield skaicius

n = 10
fibonacci_seka = list(fib_generator(n))
print("Fibonacci seka:", fibonacci_seka)

lyginiai = list(filtruoti_lyginius(fib_generator(n)))
print("Lyginiai Fibonacci skaičiai:", lyginiai)
