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
    if(first < second and first < third):
        smallest = first
    elif(second < first and second < third):
        smallest = second
    else:
        smallest = third
    return smallest

smallNumber = getLargestNumber(first, second, third)
print(f"{smallNumber} is the smallest number.")
