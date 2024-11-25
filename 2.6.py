a = int(input("введите число от 3 до 20: "))

for i in range(1, a + 1):
    for j in range(i, a + 1):
        if a % (i + j) == 0:
            print(f"{i} {j}", end=' ')