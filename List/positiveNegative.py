#WAP to read an array and display first all positive numbers and then all negative numbes.

myList = [12,3,33,34,45,33,64,65,22,98,88,33,22,97,45]

positive = list()
negative = list()
for num in myList:
    if(num%2 == 0):
        positive.append(num)
    else:
        negative.append(num)
positive.extend(negative)
print(positive)
