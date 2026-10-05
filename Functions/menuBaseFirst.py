first = int()
second = int()
third = int()
try:
    first = int(input("Please enter first number: "))
    second = int(input("Please enter second number: "))
    third = int(input("Please enter third number: "))
    action = input("Please enter a action. For Largest enter largest. For smallest enter smallest. For sort enter sort : ")

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

def getSmallestNumber(first, second, third):
    if(first < second and first < third):
        smallest = first
    elif(second < first and second < third):
        smallest = second
    else:
        smallest = third
    return smallest

def getSecondSmallestNumber(first, second, third):
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

def getSortedValues(first, second, third):
    largest = getLargestNumber(first, second, third)
    secondLargest = getSecondSmallestNumber(first, second, third)
    smallest = getSmallestNumber(first, second, third)

    result = [smallest, secondLargest, largest]
    return result

def typeAction(action):
    match action:
        case "largest":
            result = getLargestNumber(first, second, third)
            return result
        case "smallest":
            result = getSmallestNumber(first, second, third)
            return result
        case "sort":
            result = getSortedValues(first, second, third)
            return result
        case _:
            return "not enter a valid action"
    

lastResult = typeAction(action)
print(f"{lastResult} is the {action} number.")
