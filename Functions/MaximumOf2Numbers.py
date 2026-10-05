first = int()
second = int()
try:
    first = int(input("Please enter first number: "))
    second = int(input("Please enter second number: "))

except ValueError:
    print("Error: The file contents could not be converted to an integer.")

def getLargestNumber(first, second):
    if(first > second):
        largest = first
    else:
        largest = second
    return largest

largNumber = getLargestNumber(first, second)
print(f"{largNumber} is the largest number.")
