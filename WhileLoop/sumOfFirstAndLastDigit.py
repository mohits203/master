num = int(input("Enter a digit : "))
last = num%10
first = int()
while(num != 0):
        first = num%10
        num = int(num/10)
sum = first+last
print(f"first and last digit sum is : {sum}")
