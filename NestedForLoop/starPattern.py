n = int(input("Please enter a number : "))

for i in range(1, n+1):
    k = i
    if(i%2 != 0):
        k -= 1
    for j in range(1, k):
        print("*", end="")
    print()
