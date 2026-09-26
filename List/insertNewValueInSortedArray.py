'''Write a program in C to insert the values in the array (sorted list).
Test Data :
Insert New value in the sorted array :
-----------------------------------------
Input the size of array : 5
Input 5 elements in the array in ascending order:
element - 0 : 2
element - 1 : 5
element - 2 : 7
element - 3 : 9
element - 4 : 11
Input the value to be inserted : 8
The exist array list is :
2 5 7 9 11
After Insert the list is :
2 5 7 8 9 11'''

userList = []
for i in range(1,5):
    num = int(input("Enter the number you want to store in a array : "))
    userList.append(num)

print(f"original list : {userList} ")
userListCopy = userList.copy()
insertVal = int(input("Enter the value which one insert : "))
isInsert = True
for index, value in enumerate(userList):
    if(value > insertVal and isInsert):
        userList.insert(index, insertVal)
        isInsert = False

if(len(userList) == len(userListCopy) and isInsert):
    userList.append(insertVal)



print(f"After insert new value in sorted order : {userList}")

