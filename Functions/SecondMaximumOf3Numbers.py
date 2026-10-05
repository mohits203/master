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
        if(second > third):
            secLarge = second
        else:
            secLarge = third
    elif(second > first and second > third):
        if(first > third):
            secLarge = first
        else:
            secLarge = third
    else:
        if(first > second):
            secLarge = first
        else:
            secLarge = second
    return secLarge

secLargNumber = getLargestNumber(first, second, third)
print(f"{secLargNumber} is the second largest number.")
