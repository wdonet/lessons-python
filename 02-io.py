# run this from console as 
# $ python3 02-io.py one two three

from sys import argv
from os.path import exists

script, first, second, third = argv

name = input("name (txt): ")
print('age (number):', end=' ')
age = int(input())
print (f"Hi {name} of {age} years old")
print (f"""
 Also you provided values with {script}:
 - {first}
 - {second}
 - {third}
 """)

# files
filename = '02-io-sample.txt'
txt = open(filename)
print(txt.read())
## read line by line
txt.seek(0)  # go back to the begining
print("\nFirst line: [{}]".format(txt.readline()))
txt.close()

print("Exist file ? {}".format(exists(filename)))
txt = open(filename, 'w') # mode: w,r,+,t,b,x
txt.truncate() # empty file
content = """This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
"""
txt.write(content)
txt.close()
