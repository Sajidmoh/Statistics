print("Statistics")
print("Program to find out mean median and mode for given numnbers\n")

def getMean (numbers):
    sum = 0
    for i in range(len(numbers)):
        sum = numbers[i]+sum
    mean = sum / len(numbers)  
    return mean
  
def getMedian(numbers):
    numbers.sort()

    
    if len(numbers)%2 == 0:
        mid = len(numbers)//2
        previous = mid - 1
        median = (numbers[mid] + numbers[previous])/2

        return median
      
    else:
        return numbers[len(numbers)//2]

def getMode(lst):
    uniquelst = []
        
    for i in range(len(lst)): 
      if lst[i] not in uniquelst:
        uniquelst.append(lst[i])

    maxrep = 0
    mode = uniquelst[0]
    for i in uniquelst:
        rep = lst.count(i)
        if rep > maxrep:
            maxrep = rep
            mode = i    
    return mode       

#main program
def getRange(numbers):
    numbers.sort()
    range = numbers[-1] - numbers[0]
    return range

def getMeanDeviation(numbers):
    mean = getMean(numbers)
    deviations = []
    for i in range (len(numbers)):
        deviation = abs(numbers[i] - mean)
        deviations.append(deviation)
    meanDeviation = getMean(deviations)
    return meanDeviation

def getMeanDeviationAboutMedian(numbers):
    deviations = []
    median = getMedian(numbers)
    for i in range (len(numbers)):
        deviation = abs(numbers[i] - median)
        deviations.append(deviation)
    meanDeviationAboutMedian = getMean(deviations)
    return meanDeviationAboutMedian






def getStandardDeviation(numbers):
    mean  = getMean(numbers)
    deviations = []
    for i in range (len(numbers)):
        deviation = (numbers[i] - mean)**2
        deviations.append(deviation)
    standardDeviation = (getMean(deviations))**0.5    
    return standardDeviation



values = []#10/2 = 5 5+1=6 a[6] -a[5] = d a[5] + d 
amount=int(input("How many numbers would you like to input "))
for i in range (amount):
    obs = int(input("enter number: "))
    values.append(obs)

print("\nResults\n")

print("mean: ",getMean(values))
print("Median: ",getMedian(values))
print("mode: ", getMode(values))
print("Range: ", getRange(values))
print("mean deviation: ",getMeanDeviation(values))
print("mean deviation about median: ",getMeanDeviationAboutMedian(values))
print("Standard deviation: ",getStandardDeviation(values))  