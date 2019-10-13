# The number to perform the Collatz operation.
n = 20

# Keep looping until n = 1 assuming Collatz conjecture is true.
while n != 1:
    print(n)  # print current value of n.
    if n % 2 == 0:  # if even, divide by two.
        n /= 2
    else:  # if odd, multiply by three and add one.
        n = (3 * n) + 1

# Print last value of n (should be 1)
print(n)
