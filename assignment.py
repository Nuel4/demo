result= True

while result:
    num = int(input('enter a number :'))
    if num %2 !=0:
        result=True
    else:
        print('Correct ! That is the correct number')
        result =False

def code_maker(mystring):
    '''
     INTPUT :is a string
     OUTPUT: same string but all vowels are converted to  *
    '''
    output =list(mystring)
    for i ,letter in enumerate(mystring):
        for vowel in ['a','e','i','o','u']:
            if letter.lower() == vowel:
                output[i] = '*'

    output =''.join(output)
    return output
# different output formation
print('.........................')
def code_mak(mystring):
    '''
     INTPUT :is a string
     OUTPUT: same string but all vowels are converted to  *
    '''
    output =list(mystring)
    for i ,letter in enumerate(mystring):
        for vowel in ['a','e','i','o','u']:
            if letter.lower() == vowel:
                output[i] = '*'


    return output


print('.........................')
def code_making(mystring):
    '''
     INTPUT :is a string
     OUTPUT: same string but all vowels are converted to  *
    '''
    output =list(mystring)
    for i ,letter in enumerate(mystring):
        for vowel in ['a','e','i','o','u']:
            if letter.lower() == vowel:
                output[i] = '*'

    output = '-x12'.join(output)
    return output



res = code_maker('EMMANUEL CHUKWUOKOLO')
print(res)
print('..........without .join function...............')
re =code_mak('EMMANUEL')
print(re)
r =code_making('Chukwudi')
print(r)

