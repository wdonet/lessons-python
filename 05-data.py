#!/usr/bin/python3

## Arrays or Lists

# /v is a vertical tab
# [1:4] a slice of the array
# join helps to join elements in an array with a separator between
strs = ['a','b','c','d','e','f']
print(f"\vjoin => {'#'.join(strs[1:4])}")

print('-' * 10) # repeat "-" 10 times

## Dictionaries
person = {
  'name': 'John',
  'age': 39,
  'height_in_cm': 183
}
person[0] = 'Jhonny'
print(f"{person['name']} is {person['height_in_cm']}cm tall")
print(f"Alias {person[0]}.")
print(person, end='\n\n')
# get dictionary elements as tuples array
print(list(person.items())[0])
print(f"""\vGET\n
 {person.get('name')}
 and {person.get('noExists')}
 and {person.get('noExists', '[use default value if no exist]')}
""")