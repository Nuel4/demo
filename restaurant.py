indian =['Briani' ,'Dosa' ,'Chapatti']
chinese =['Egg roll' ,'Pot sticker' ,'Fried rice']
italian = ['Pizza' ,'Pasta' ,'Risotte']
nigerian =['Jellof rice' ,'Moimoi' ,'Yam']

dishes = input('Enter your order :').capitalize()

if dishes in indian:
    print("Indian food -> " ,dishes)

elif dishes in italian:
    print('Italin food -> ' ,dishes)

elif dishes in chinese :
    print('Chinese food - > ' ,dishes)

elif dishes in nigerian:
    print("Nigerian food -> " ,dishes)

else:
    print(" Your choice of food not avaible here")

