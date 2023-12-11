# CTI-110
# P2HW2 - List
# Terrell Locks
# October 22, 2023
#

#user inputs the grades as floats

Module1 = float(input('Enter Grade for Module 1: '))
Module2 = float(input('Enter Grade for Module 2: '))
Module3 = float(input('Enter Grade for Module 3: '))
Module4 = float(input('Enter Grade for Module 4: '))
Module5 = float(input('Enter Grade for Module 5: '))
Module6 = float(input('Enter Grade for Module 6: '))
print('\n------------Results------------')

#all inputs are added to a list

all_scores = [Module1, Module2, Module3, Module4, Module5, Module6]

#the list is calculated as a variable

average = (Module1 + Module2 + Module3 + Module4 + Module5 + Module6) / 6

print(f'{"Lowest Grade:"}        {min(all_scores)}')
print(f'{"Highest Grade:"}       {max(all_scores)}')
print(f'{"Sum of Grade:"}        {sum(all_scores)}')
print(f'{"Average:"}             {average:.2f}')
print('-------------------------------------------')

#IDLE displayed the grades of the lists using the "min, max and sum" operations
#average is displayed and rounded to the nearest tenth
