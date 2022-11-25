print('Welcome to the palindrome checker:')

word = input('Please enter your word:').lower()

reversed_word = word[::-1]
if word == reversed_word:
    print('Your word is a Palindrome')
elif word:
    print('Your word is not a Palindrome')