'''Find the Missing Number
Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.

Note: There are no duplicates in the list.

Examples: 

Input: arr[] = {1, 2, 4, 6, 3, 7, 8}
Output: 5
Explanation: Here the size of the array is 7, so the range will be [1, 8]. The missing number between 1 to 8 is 5

Input: arr[] = {1, 2, 3, 5}, N = 5
Output: 4
Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4'''

listLen = int(input("Enter the list length number : "))

userList = []
for i in range(1,listLen+1):
    num = int(input("Enter the number you want to store in a array (Note: There are no duplicates in the list) : "))
    userList.append(num)

print(f"original list : {userList} ")
missVal = int()
for r in range(1, len(userList)+1):
    if(userList.count(r) == 0):
        missVal = r
        exit
        
print(f"Missing value is : {missVal}")

