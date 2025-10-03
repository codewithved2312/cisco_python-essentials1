# collatz hypothesis
n = int(input("Enter an integer: "))
steps = 0

while n > 1:
    if n % 2 == 0:
        n = n // 2
    elif n % 2 != 0:
        n = 3 * n + 1
    steps += 1
    print(n)
    
print("Steps: ", steps)
