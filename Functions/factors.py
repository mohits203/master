num = int()
try:
    num = int(input("Please enter a number: "))

except ValueError:
    print("Error: The file contents could not be converted to an integer.")

fac = list()
def getFactor(num):
    for n in range(1, num+1):
        if(num%n == 0):
            fac.append(n)
    return fac

factors = getFactor(num)

print(f"{factors} is the factors of {num}.")
