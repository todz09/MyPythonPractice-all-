n = 28
divisor_sum = sum(i for i in range(1, n) if n % i == 0)
print(f"{n} is a perfect number" if divisor_sum == n else f"{n} is not a perfect number")
