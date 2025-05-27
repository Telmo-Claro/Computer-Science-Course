word = input("String: ").lower().strip(" , . ? ! ;")

# empty string to store the reversed word
reversed = ""

# Sets the x as the length of the word and -1 because python starts with 0 (0, 1, 2) and now it's (1, 2, 3)
x = len(word) - 1

#  while x is the same or greater than 0
while x >= 0:
    # Will build the new reversed word
    reversed += word[x]
    # Proceeds to another letter
    x -= 1

if word == reversed:
    # This code is checking whether the input word is a palindrome or not.
    print(f'"{word}" is a palindrome')
else:
    print(f'"{word}" is not a palindrome')
