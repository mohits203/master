#WAP to read an array and display first all positive numbers and then all negative numbes.

listLen = int(input("Enter the list length number : "))

positive = []
negative = []
for i in range(1,listLen+1):
    num = int(input("Enter the number you want to store in a array : "))
    if(num > 0):
        positive.append(num)
    else:
        negative.append(num)
positive.extend(negative)
print(positive)
print(negative)
