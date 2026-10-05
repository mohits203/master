first = int()
second = int()
third = int()
try:
    first = int(input("Please enter first number: "))
    second = int(input("Please enter second number: "))
    third = int(input("Please enter third number: "))

except ValueError:
    print("Error: The file contents could not be converted to an integer.")

def getLargestNumber(first, second, third):
    if(first > second and first > third):
        largest = first
    elif(second > first and second > third):
        largest = second
    else:
        largest = third
    return largest

largNumber = getLargestNumber(first, second, third)
print(f"{largNumber} is the largest number.")
