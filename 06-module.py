#!/usr/bin/python3

import module
from random import randint, sample

print(f"Sum 4 + 5 = {module.sum(4,5)}")
print(f"Name is {module.name}")

person = module.Person.parse_person('Jane')
defPerson = module.Person()
print(f'\v The default person is {defPerson.get_name()}')
print(f' The new person is {person.get_name()}')

words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
count = randint(1, 10)
print('random number {}\n and selected word {}'.format(count, words[count]))
print(f"sample word = {sample(words, count)}")