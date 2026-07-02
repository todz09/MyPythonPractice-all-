n = 153
digits = len(str(n))
'print(f"{n} is an Armstrong number" if sum(int(d)**digits for d in str(n)) == n else f"{n} is not an Armstrong number")'
armstrong_sum = sum(int(digit) ** digits for digit in str(n))
if armstrong_sum == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
