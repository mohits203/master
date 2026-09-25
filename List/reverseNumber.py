#WAP to read an array and display reverse of all numbers in array

myList = [12,3,33,34,45,33,64,65,22,98,88,33,22,97,45]

reverse = list()
for num in myList:
    reverse.insert(0,num)
print(reverse)


#or by using reverse method
print(type(myList))
myList.reverse()
print(myList)
