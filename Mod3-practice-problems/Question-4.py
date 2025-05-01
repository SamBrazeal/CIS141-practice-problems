#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
sliceWord = input("Please input a word: ")
sliceIndex1 = int(input("Please input a number: "))
sliceIndex2 = int(input("Please input another number: "))

WordSliced = sliceWord[sliceIndex1:sliceIndex2]

print(f"Your word sliced: \n{WordSliced}")
