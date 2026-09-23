n = int(input("Please enter a number : "))
r = n+1
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(r-j, end="")
    print()
