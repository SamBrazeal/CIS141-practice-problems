# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. 
# Use the skills you learned in this module to print the word the correct number of times.
Name = input("what is your name: ")
Age = input("what is your age: ")

Age_up = int(Age) + 1

print("Hello, " + Name + "! You are " + Age + " years old. Next year, you will be " + str(Age_up) + " years old.")
