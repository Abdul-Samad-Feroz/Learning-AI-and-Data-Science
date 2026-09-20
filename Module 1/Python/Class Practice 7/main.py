numbers = [10,20,30,40,50,60,70,80]

print(numbers[0:8:2])

print(numbers[0:5:1]) #[Start,Stop,Step]

numbers[-1:-5:-1]

word = []
word = input("Enter a word: ")

if word == word[::-1]:
    print("It's a Palindrom")
else:
    print("Not a Palindrom")    


