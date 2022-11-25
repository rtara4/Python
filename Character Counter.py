print('Welcome to the sentence analyser')

sentence_input = input('Please enter your sentence:')

consonants = ('b', 'B', 'c', 'C', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'H', 'j', 'J', 'k', 'K' , 'L', 'l', 'm', 'M' , 'n', 'N', 'p', 'P', 'q', 'Q' , 'r', 'R', 'S', 's', 't', 'T', 'v', 'V', 'w', 'W' 'x', 'X', 'y', 'Y', 'z', 'Z')
consonant_count = 0
for letter in sentence_input:
    if letter in consonants:
        consonant_count += 1 

vowels = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')
vowel_count = 0
for letter in sentence_input:
    if letter in vowels:
        vowel_count += 1

numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
number_count = 0
for letter in sentence_input:
    if letter in numbers:
        number_count += 1

punctuation = (')', '(', '*', '&', ',', '.', '.', '@', '!', '"', '£', ':', ';', '<', '>',)
punctuation_count = 0
for letter in sentence_input:
    if letter in punctuation:
        punctuation_count += 1
        
white_space = ('\',''  ')
white_space_count = 0
for letter in sentence_input:
    if letter in white_space:
        white_space_count += 1
        
print('Number of consonants :', consonant_count)
print('Number of vowels :', vowel_count)
print('Number of numbers :', number_count)
print('Number of white space :', white_space_count)
print('Number of punctuation :', punctuation_count)
