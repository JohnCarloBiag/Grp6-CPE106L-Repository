"""
A group of statisticians at a local college has asked you to create a set of functions that compute the median and mode of a set of numbers, as defined in the below sample programs:
· mode.py
· median.py
Define these functions in a module named stats.py. Also include a function named mean, which computes the average of a set of numbers. Each function should expect a list of numbers as an argument and return a 
single number. Each function should return 0 if the list is empty. Include a main function that tests the three statistical functions with a given list.
"""

def main():

    numbers = []
    userInput = input("Enter elements: ")
    if len(numbers) == None:
        median(numbers)
        mode(numbers)
        mean(numbers)
    else:
        elements = userInput.split()
        for i in elements:
            numbers.append(int(i))
        median(numbers)
        mode(numbers)
        mean(numbers)
    
def median(numbers):
    if len(numbers) == 0:
        return 0
    else:
        numbers.sort()
        midpoint = len(numbers) // 2
        print("The median is", end =" ")
        if len(numbers) % 2 == 1:


            print(numbers[midpoint])
        else:
            numbers = int ((numbers[midpoint] + numbers[midpoint - 1]) /2)

            print(numbers)
def mode(numbers):
    if len(numbers) == 0:
        return 0
    else:
        numberDictionary = {}
        for i in numbers:
            number = numberDictionary.get(i, None)
            if number == None:
                numberDictionary[i] = 1
            else:
                numberDictionary[i] = number + 1
        
        theMaximum = max(numberDictionary.values())
        for key in numberDictionary:
            if numberDictionary[key] == theMaximum:
                print("The mode is", key)
                break
def mean(numbers):
    if len(numbers) == 0:
        return 0
    else:
        sum = 0
        for i in range(0, len(numbers)):
            sum = sum + numbers[i]
        number = int(sum/len(numbers))
        print("The mean is", number)

if __name__ == "__main__":
    main()
