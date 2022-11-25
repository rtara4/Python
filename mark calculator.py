print('Welcome to the python mark calculator')


first_mark = float(input('Input the first mark'))
first_weight = float(input('Input the weight of the first mark'))

second_mark = float(input('Input the second mark'))                     
second_weight = float(input('Input the weight of the second mark'))                                

third_mark = float(input('Input the third mark'))                     
third_weight = float(input('Input the weight of the third mark'))                                

print ('The overall mark for the marks and the weight input is:')

divided_weight1 = (first_weight/100)
divided_weight2 = (second_weight/100)
divided_weight3 = (third_weight/100)

first_total = (first_mark*divided_weight1)
second_total = (second_mark*divided_weight2)
third_total = (third_mark*divided_weight3)

print('Mark 1=',first_mark,'x',divided_weight1, '=', first_total)
print('Mark 2=',second_mark,'x',divided_weight2, '=', second_total)
print('Mark 3=',third_mark,'x',divided_weight3, '=', third_total)

total_overall = (first_total + second_total + third_total)
print('The overall mark is:', first_total,'+', second_total, '+', third_total, '=', total_overall,)