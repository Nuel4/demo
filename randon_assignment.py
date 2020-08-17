import random
newpass ='no'
rand = random.randint(10000 ,99999)
while newpass =='no':

    first_name =input("enter your first name:")
    first =first_name[:2]
    last_name =input("Enter your last name")
    last =last_name[:2]
    email =input("Enter your email")
    password =first+last+ str(rand)
    print( "This is your password :" , password)

    newpass =input("Are you ok with the password?")
    if newpass:
        password=input(" enter a new passward:")


print(" Congratulations,your passward is ok")





