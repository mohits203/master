'''Find duplicates in O(n) time and O(1) extra space | Set 1
Given an array of n elements that contains elements from 0 to n-1, with any of these numbers appearing any number of times. Find these repeating numbers in O(n) and use only constant memory space.

Note: The repeating element should be printed only once.

Example: 

Input: n=7 , array[]={1, 2, 3, 6, 3, 6, 1}
Output: 1, 3, 6
Explanation: The numbers 1 , 3 and 6 appears more than once in the array.

Input : n = 5 and array[] = {1, 2, 3, 4 ,3}
Output: 3
Explanation: The number 3 appears more than once in the array.'''

listLen = int(input("Enter the list length number : "))

userList = []
for i in range(1,listLen+1):
    num = int(input("Enter the number you want to store in a array (Note: There are no duplicates in the list) : "))
    userList.append(num)

print(f"original list : {userList} ")
dupList = list()
for value in userList:
    if(userList.count(value) > 1 and dupList.count(value) == 0):
        dupList.append(value)
        
print(f"Duplicates value is : {dupList}")

