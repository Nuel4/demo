book ={}

book['Bob'] ={
    'name':'Bob',
    'Address':'lagos state',
    'age':23,
    'phone': 5688898
}

book['Mark'] ={
    'name':'Mark',
    'Address':'Enugu state',
    'age':25,
    'phone':6567999666
}
import  json
s =json.dumps(book)
with open("C:\\Users\emman\Desktop\ book.txt" ,'w') as f:
    f.write(s)