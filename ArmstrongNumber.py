n = int(input('Enter a number:'))
sum = 0
temp = n
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if n == sum:
   print(n,'Is an Armstrong number')
else:
   print(n,'Is not an Armstrong number')
