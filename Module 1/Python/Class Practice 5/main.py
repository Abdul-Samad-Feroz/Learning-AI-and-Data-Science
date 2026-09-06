# Smallest Number
number = int(input("Enter a Number:"))
smallest = number

for i in range(4):
    number = int(input("Enter a Number:"))
    if number < smallest:
        smallest = number
print("smallest:", smallest)

# Looping through strings
word = "Pakistan"
for letter in word:
    print(letter)


word = input("Enter A Word: ")
count = 0
for letter in word:
    if letter == "a" or letter == "A":
        count += 1
print("Number of A Characters:", count)

word = input("Enter A Word: ").lower()
count = 0
for letter in word:
    if (
        letter == "a"
        or letter == "e"
        or letter == "i"
        or letter == "o"
        or letter == "u"
    ):
        count += 1
print("Number of vowels:", count)
# Best Practice
word = input("Enter a sentence/word: ")
count = 0
for letter in word:
    if letter in "aeiouAEIOU":
        count += 1
print(count)

test_input = input("Enter something: ").lower()
print(test_input)


sentence = input("Enter a sentence/word: ")
count = 0
for i in sentence:
    if i == " ":
        count += 1
print(count)

word = input("Enter a sentence/word: ").lower()
chars = 0
vowels = 0
consonats = 0
letter_a = 0
for letter in word:
    chars += 1
    if letter in "aeiouAEIOU":
        vowels += 1
    else:
        consonats += 1
    if letter == "a":
        letter_a += 1

print("Consonants:", consonats)
print("Vowels:", vowels)
print("Charactes:", chars)
print("Number of a's:", letter_a)
