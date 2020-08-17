from pathlib import Path
pat1 =Path('ecommerce')
print(pat1.exists())

pat =Path('emails')
print(pat.mkdir()) # make directory
#print(pat.rmdir())  # to remove a directory