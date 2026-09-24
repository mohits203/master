n = int(input("Please enter a number : "))
k = 1
for i in range(1, n+1):
    for j in range(1, i):
        print(k, end="")
        k +=1
    print()
