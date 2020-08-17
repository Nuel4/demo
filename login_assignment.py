import random
newpass ='no'
rand = random.randint(10000 ,99999)
lst =[]
def login():

    first_name =input("enter your first name:")
    first =first_name[:2]
    last_name =input("Enter your last name")
    last =last_name[:2]
    email =input("Enter your email")
    password =first+last+ str(rand)
    print( "This is your password :" , password)

    newpass =input("Are you ok with the password?")
    if newpass=='yes':
        
        print(first_name,'\n',last_name ,'\n' ,email)
        lst.append([first_name, last_name, email, password])

    else:
         password =input('enter your password:')
         while len(password) < 7:
             print("password should be more than 7")
             password=input("re-enter your password")

         else:

             print(" Congratulations,your passward is accepted")
             print("first name:",first_name)
             print("last name:",last_name )
             print("Email :",email)
             print("password :" ,password)
             lst.append([first_name,last_name ,email,password])

login()
print(lst)