#1. Prompt the user for a positive integer n. Use a while loop to 
#sum all the integers from 1 up to n. Print the final sum.

n = int(input("Please input a positive integer: "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("The sum of all integers from 1 to", n, "is:", total)
