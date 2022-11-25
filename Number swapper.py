print('Welcome to the number swapper') #This statement welcomes the user into the number swapper

number_one = float(input("Enter your first number here: ")) #This question asks the user for a number. It uses input so they can add a number and a float so a decimal can be included
number_two = float(input("Enter your second number here: ")) #This question asks the user for a number. It uses input so they can add a number and a float so a decimal can be included


if number_one > number_two: 
    print('Your numbers were swapped')
    print('The smaller number was', number_two)
    print('The bigger number was', number_one)
if number_two > number_one:
    print('Your numbers were notswapped')
    print('The smaller number was', number_one)
    print('The bigger number was', number_two)
if number_one == number_two:
    print('Your numbers are the same')
    print(number_1, 'is equal to',number_two,)