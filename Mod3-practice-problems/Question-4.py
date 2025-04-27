sliceWord = input("Please input a word: ")
sliceIndex1 = int(input("Please input a number: "))
sliceIndex2 = int(input("Please input another number: "))

wordSlice1 = sliceWord[:sliceIndex1]
wordSlice2 = sliceWord[sliceIndex1:sliceIndex2]
wordSlice3 = sliceWord[sliceIndex2:]

print(f"Your word sliced: \n{wordSlice1} \n{wordSlice2} \n{wordSlice3}")
