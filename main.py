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

    mid = len(numbers)/2
    
    if len(numbers)%2 == 0:
        d = numbers[int(mid+1)] - numbers[int(mid)]
        d = d/2
        median = numbers[int(mid)]
        median = median - d
        return median
      
    else:
        return numbers[int(mid)]

#main program
values = []#10/2 = 5 5+1=6 a[6] -a[5] = d a[5] + d 
amount=int(input("How many numbers would you like to input "))
for i in range (amount):
    obs = int(input("enter number: "))
    values.append(obs)

print("mean: ",getMean(values))
print("Median: ",getMedian(values))



  