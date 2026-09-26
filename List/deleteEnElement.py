'''Write a program in C to delete an element at a desired position from an array.
Test Data :
Input the size of array : 5
Input 5 elements in the array in ascending order:
element - 0 : 1
element - 1 : 2
element - 2 : 3
element - 3 : 4
element - 4 : 5
Input the position where to delete: 3
Expected Output :
The new list is : 1 2 4 5'''

userList = []
for i in range(1,6):
    num = int(input("Enter the number you want to store in a array : "))
    userList.append(num)

print(f"original list : {userList} ")

deleteVal = int(input("Enter the value which one need to delete : "))
userList.remove(deleteVal)



print(f"After delete value in sorted order : {userList}")

