'''Use for loop to iterate from 0 to 100 and
print the sum of all evens and the sum of all odds. '''

Even_nums = 0
odd_nums = 0
for item in range(0,101):
    if item % 2 == 0:
        Even_nums +=item
    else:
        odd_nums+=item

print(f"The sum of all even is {Even_nums} and the sum of all odds is {odd_nums}")

