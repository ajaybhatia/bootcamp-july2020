from math import floor, sqrt

limit = 10000000

nums, primes = [], []

# Initialize nums to True for all odd indices
for i in range(limit):
    if i % 2 == 0 and i != 2:
        nums.append(False)
    else:
        nums.append(True)


i = 2
while i*i <= limit:
    if nums[i] == True:
        j = i**2
        while j <= limit:
            try:
                nums[j] = False
            except:
                pass
            j += i
    i += 1

for x in range(2, limit):
    if nums[x] == True:
        primes.append(x)


# i = 0
# while primes[i] < sqrt(limit):
#     if limit % primes[i] == 0:
#         print(primes[i])
#     i += 1
print(primes)
