print('Welcome to the leap year calculator')
year = int(input('Please enter the year: '))


if (year %400 == 0) and (year %100 == 0):
    print(year, ' is a leap year')
    
elif (year %4 == 0) and (year %100 != 0):
    print(year, ' is a leap year')
        
else:
     print(year,'is not a leap year')
    