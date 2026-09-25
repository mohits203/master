#wap to read an array and search a value in it , if present then show position where it is present , as the element can be present more than one time so show all positions and also the count of times it is present
myList = [12,3,33,34,45,33,64,65,22,98,88,33,22,97,45]

searchNum = int(input("Enter the number you want to search : "))
indexNum = []
if(myList.count(searchNum) > 0):
    for index, value in enumerate(myList):
        if(value == searchNum):
            indexNum.append(index)
    print(f"Total {myList.count(searchNum)} records found. Positions are {indexNum}")

else:
    print("not found")

