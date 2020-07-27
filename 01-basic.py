# Print
print("Hello " + "World !")
# Comments go here
print("🌎")

# Math Operators: (),+,-,/,//,*,%,<,>,<=,>=,==
print("3+2 < 5-7 =", (3 + 2) < 5 - 7)
print("10%30", "=", 33 % 10)
print("343.5%100", "=", 343.5 % 100)
print("6.0*4", "=", 6.0*4)
print("2^3", "=", 2**3)

# Variables
person_age = 24
print("John is", person_age, "years old")
person_age = round(84.5)
print(f"and his father is {person_age} years old") #format string
mother = """and,
his mother is only {}
and,
she's {} tall""" # three double quotes 
print(mother.format(79, '158cm'))

print('.' * 10)
ch1 = 'o'
ch2 = 'n'
ch3 = 'e'
print(ch1 + ch2 + ch3, end='.\n\'\t.\n') #escaping chars
formatter = '>{}{}'
print(formatter.format(True, formatter))

