# Looping for

n = 10
while n > 0:
    print(n)
    n = n - 1
print('Fire!')


n = 0
while n <= 10:
    if n < 5:
        print(n, "it's smaller than 5")  # é menor que
    elif n == 5:
        print(n, "it's the same as 5")  # é igula a
    else:
        print(n, "is bigger than 5")  # é maior que
    n = n + 1
