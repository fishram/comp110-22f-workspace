"""EX01 - Chardle - A cute step toward Wordle.

 ///   __author__ = "730575695"""

word: str = input("Enter a 5-character word: ")
if(len(word) != 5):
    exit()
character: chr = input("Enter a single character: ")
if(len(character) != 1):
    exit()
char_counter: int = 0
print("Searching for "+character+" in "+word)
if(word[0] == character):
    print(character+" found at index 0")
    char_counter = char_counter+1

if(word[1] == character):
    print(character+" found at index 1")
    char_counter = char_counter+1

if(word[2] == character):
    print(character+" found at index 2")
    char_counter = char_counter+1

if(word[3] == character):
    print(character+" found at index 3")
    char_counter = char_counter+1

if(word[4] == character):
    print(character+" found at index 4")
    char_counter = char_counter+1

if(char_counter == 0):
    print("No instances of "+character+" found in"+ word)

else:
    print(char_counter+" instances of "+character+" found in "+ word)


    

