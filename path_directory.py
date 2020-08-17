from pathlib import Path
pat1 =Path('ecommerce')
#print(pat.exists())

#pat =Path('emails')
#print(pat.mkdir()) # make directory
#print(pat.rmdir())  # to remove a directory
pat = Path()
print(pat.glob(' *.py '))
for files in pat.glob('*.py'): # all python files in the directory
    print(files)
print("..........................")
for fil in pat.glob('*'):
    print(fil)