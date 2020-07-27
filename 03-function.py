def add_two(*args):
  a, b = args
  print(f"Operating with: {a}, {b}")
  return a + b

print(f"\nsum is {add_two(1, 2)}")
print(f"sum is {add_two(-1, -2)}\n")
# print(f"sum is {add_two(1, '2')}") #fails bc str

def filterNumericPairs(str):
  pairs = []
  for numStr in str.split():
    number = int(numStr)
    # conditionals: and, or, not, !=,==,>=,<=
    if number % 2 is 0:  # "==" same as "is"
      pairs.append(number)
  return pairs

pairs = filterNumericPairs('1 4 7 4 2 23 0')
print(f'\nPairs {pairs}')

def findNumber(num, array):
  if num in array:
    return f'{num} at array: {array}'
print(f'\nFound {findNumber(7, [1, 4, 7, 4, 2, 23, 0])}\n')

def fizzBuzz(limit):
  fizz = []
  buzz = []
  fibuzz = []
  numbers = []
  # range(init, end, step) for a sequence of numbers
  for num in range(0, limit, 1):
    if num % 15 == 0:
      fibuzz.append(num)
      print('FizzBuzz')
    elif num % 3 == 0:
      fizz.append(num)
      print('Fizz')
    elif num % 5 == 0:
      buzz.append(num)
      print('Buzz')
    else:
      numbers.append(num)
      print(num)

  return fizz, buzz, fibuzz, numbers

f, b, fb, n = fizzBuzz(20)
print('Results \n Fizz{} \nBuzz{} \nFizzBuzz{} \nRest{}'.format(f, b, fb, n))

# lambda (anonymous fn)

exp2 = lambda num: num ** 2
print(f'\nLambda\n\tExp 2 of {2} is {exp2(2)}')
