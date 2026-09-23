num = int(input("Please enter a digit : "))

x = 0
while(num !=0):
    x = x*10 + num%10
    num = int(num/10)
print(x)
