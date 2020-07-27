from sys import argv
from os.path import exists

script, from_file, to_file = argv

if exists(from_file):
  if exists(to_file):
    print(f'Error: {to_file} already exists')
  else:
    target = open(to_file, 'w')
    source = open(from_file)
    target.write(source.read())
    source.close()
    target.close()
    ## this line do the same bc python closes files
    # open(to_file, 'w').write(open(from_file).read())
    print('OK. Copied.')
else:
  print(f'Error: {from_file} do not exists')

# Try this at console:
# $ python3 02.1.copy.py 02-io-sample.txt destino.txt