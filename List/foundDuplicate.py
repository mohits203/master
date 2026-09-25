#Write a program in python to count the total number of duplicate elements in an array.
userList = []
isDuplicate = False
for i in range(1,4):
    num = int(input("Enter the number you want to store in a array : "))
    userList.append(num)
    if(userList.count(num) > 1):
        isDuplicate = True
        duplicateNum = num

if(isDuplicate):
    print(f"duplicate number is : {duplicateNum}")
else:
    print("duplicate number not exist in list")



