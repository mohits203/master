'''Write a program in C to count the frequency of each element of an array.
Test Data :
Input the number of elements to be stored in the array :3
Input 3 elements in the array :
element - 0 : 25
element - 1 : 12
element - 2 : 43
element - 3 : 12
Expected Output :
The frequency of all elements of an array :
25 occurs 1 times
12 occurs 2 times
43 occurs 1 times'''

listLen = int(input("Enter the list length number : "))

userList = []
userListItemCount = []
for i in range(1,listLen+1):
    num = int(input("Enter the number you want to store in a array : "))
    if(userList.count(num) >= 1):
        alreadyIn = userList.index(num)
        userListItemCount[alreadyIn] = userListItemCount[alreadyIn]+1
    else: 
        userList.append(num)
        userListItemCount.append(1)



print(f"original list : {userList} ")
print(f"original list : {userListItemCount} ")
    
