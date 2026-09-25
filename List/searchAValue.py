#WAP to read an array and search a value in it, if present then show position where it is present otherwise not found.

myList = [12,3,33,34,45,33,64,65,22,98,88,33,22,97,45]

searchNum = int(input("Enter the number you want to search : "))

if(myList.count(searchNum) > 0):
    print(myList.index(searchNum))
else:
    print("not found")
