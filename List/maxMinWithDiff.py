'''Write a program in C to find the maximum and minimum and maximum difference elements in an array.
Test Data :
Input the number of elements to be stored in the array :3
Input 3 elements in the array :
element - 0 : 45
element - 1 : 25
element - 2 : 21
Expected Output :
Maximum element is : 45
Minimum element is : 21
Maximum Difference = 24'''

userList = []
maximum = int()
minimum = 1000000000
for i in range(1,4):
    num = int(input("Enter the number you want to store in a array : "))
    userList.append(num)
    if(num > maximum):
        maximum = num
    if(num < minimum):
        minimum = num

diff = maximum - minimum

print(f"Maximum element is : {maximum}, Minimum element is : {minimum}, Maximum Difference = {diff}")

