for num in range(1, 10000):
    sum = 0
    for s_digit in str(num):
        sum += int(s_digit)**len(str(num))
    if sum == num:
        print(num, end=", ")


# for num in range(1, 100000):
#     sum, temp = 0, num
#     size = len(str(num))
#     while temp > 0:
#         digit = temp % 10
#         sum += digit**size
#         temp //= 10
#     if sum == num:
#         print(num, end=" ")
