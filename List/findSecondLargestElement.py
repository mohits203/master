'''Write a program in C to find the second largest element in an array.
Test Data :
Input the size of array : 5
Input 5 elements in the array :
element - 0 : 2
element - 1 : 9
element - 2 : 1
element - 3 : 4
element - 4 : 6
Expected Output :
The Second largest element in the array is : 6'''

userList = []
for i in range(1,6):
    num = int(input("Enter the number you want to store in a array : "))
    userList.append(num)

print(f"original list : {userList} ")

userList.sort()

print(f"The Second largest element in the array is : {userList[1]}")

