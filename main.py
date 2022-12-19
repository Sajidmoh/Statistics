print("Statistics")
print("Program to find out mean median and mode for given numnbers\n")

numbers = []#10/2 = 5 5+1=6 a[6] -a[5] = d a[5] + d 
amount=int(input("How many numbers would you like to input "))
for i in range (amount):
  obs = int(input("enter number: "))
  numbers.append(obs)

sum = 0

for i in range(len(numbers)):
  sum = numbers[i]+sum
  
mean = sum / len(numbers)  
print(mean)

numbers.sort()

mid = len(numbers)/2

if len(numbers)%2 == 0:
  d = numbers[int(mid+1)] - numbers[int(mid)]
  d = d/2
  e = numbers[int(mid)]
  e = e - d
  print(e)
  
else:
  print(numbers[int(mid)])


  