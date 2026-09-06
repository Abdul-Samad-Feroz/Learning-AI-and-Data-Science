# Smallest Number
# number = int(input("Enter a Number:"))
# smallest = number

# for i in range(4):
#     number = int(input("Enter a Number:"))
#     if number < smallest:
#         smallest = number
# print("smallest:", smallest)

#Looping through strings
word = "Pakistan"
for letter in word:
    print(letter)


word = input("Enter A Word: ")
count = 0
for letter in word:
    if letter == 'a' or letter == 'A':
        count += 1
print("Number of A Characters:", count)    

word = input("Enter A Word: ").lower()
count = 0
for letter in word:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count += 1
print("Number of vowels:", count)  

