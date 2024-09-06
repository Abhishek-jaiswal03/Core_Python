sentence = input('Enter your sentence: ')
vowels = 'aeiouAEIOU'
for char in sentence:
    if char in vowels:
        print(char, end=' ')
