#Chatbot 2
name = input("Bonjour je m'appelle Chatbot 2 et vous? ")
print(f"Bonjour {name}")
color = input("Quel est votre couleur préférée? ")
print(f"Moi aussi j'aime le {color}")
print("Quel âge avez vous?")
age = input("J'ai ... ans ")
bot_age = 11
age_diferrence = int(age) - bot_age
if int(age) > bot_age:
  print(f"J'ai {bot_age} ans et vous {age} ans vous avez donc {age_diferrence} ans de plus que moi. ")
if int(age) == bot_age: 
  print(f"J'ai {bot_age} ans et vous {age} ans vous avez donc le même âge que moi. ")
if int(age) < bot_age:
  print(f"J'ai {bot_age} ans et vous {age} ans vous avez donc {age_diferrence} ans que moi")
#Chatbot 3
humeur_1 = 1
humeur_2 = 2
humeur_3 = 3
humeur_4 = 4
print("1 = Heureux \n2 = Content \n3 = Bien \n4 = Fier")
print("Comment allez vous?")
humeur = input("Je me sens ... ")
if int(humeur) == humeur_1:
  print("Je vais bien et je suis content pour vous")
if int(humeur) == humeur_2:
  print("Je vais bien et je suis content pour vous")
if int(humeur) == humeur_3:
   print("Je vais bien et je suis content pour vous")
if int(humeur) == humeur_4:
    print("Je vais bien et je suis content pour vous")
