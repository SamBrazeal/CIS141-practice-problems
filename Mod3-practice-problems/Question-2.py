# 2. Prompt the user for their name and their age. Calculate their age next year
# Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
Name = input("what is your name: ")
Age = input("what is your age: ")

Age_up = int(Age) + 1

print("Hello, " + Name + "! You are " + Age + " years old. Next year, you will be " + str(Age_up) + " years old.")
