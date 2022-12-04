#ProgrammingProblem1
#Statisticians would like to have a set of functions to compute the median and mode of a list of numbers. The median is the number that would appear at the 
#midpoint of a list if it were sorted. The mode is the number that appears most frequently in the list. Define these functions in a module named stats.py. 
#Also include a function named mean, which computes the average of a set of numbers. Each function expects a list of numbers as an argument and returns a single number.

#stats.py module
def median(numList):
    numList.sort()
    x = len(numList)
    med = int(x / 2);
    if(x % 2 == 1):
        return numList[med]
    else:
        return (numList[med] + numList[med + 1]) / 2

def mode(numList):
    mod = max(set(numList), key = numList.count)
    return mod
    
def mean(numList):
    x = len(numList)
    sumList = 0
    for i in numList:
        sumList = sumList + i;
    return sumList / x


#main program file
import stats

numList = [27, 48, 49, 16, 3, 11, 19, 13, 29, 50]
print(stats.median(numList))
print(stats.mode(numList))
print(stats.mean(numList))
