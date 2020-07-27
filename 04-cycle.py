#!/usr/bin/python3

# for-loop
numbers = [1,2,3,4,6,9]
for number in numbers:
  print(f'=> {number}')

for number in range(0, 10, 2):
  print('Next number 2by2 is {}'.format(number))


# while-loop
index = 0
numberToFind = 3
while index < len(numbers):
  print(f'while {index}, value is {numbers[index]}')
  index += 1
