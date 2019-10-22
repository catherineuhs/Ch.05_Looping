  #Sign your name:________________

'''
 1. Make the following program work.
   '''
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    num = int(input("Enter a number: "))
    total = total + num
print("The total is:", total)
#
#


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''

# for i in range(2,101,2):
#     print(i)



'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''

# i = 10
# while i > 0:
#     print(i)
#     i -= 1
# print(i)
# print("blast off")






'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''

#
# import random
# num = random.randrange(1,11)
# print(num)
#

'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
total = 0
zero = 0
one = 0
negative = 0
for i in range(7):
    num = int(input("enter a number: "))
    total = total + num
    if num == 0:
        zero = zero + 1
    elif num > 0:
        one = one + 1
    elif num < 0:
        negative = negative +1
print("negative numbers:", negative)
print("zeros:", zero)
print("positive numbers", one)
print("the total is:", total)



