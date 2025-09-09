# for i in range(21):
#     if i % 3 == 0:
#         continue
#     print(i)


# for i in range(1, 51):
#     if(i % 2 == 0):
#         print(i)
#     if(i % 13 == 0):
#         break


num = int(input('ENter num : '))
sum = 0
while num != 0:
    sum = sum + num % 10
    num = num // 10

print('Sum is : ',sum)