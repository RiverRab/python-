# !/usr/bin/env python3
# var = "Le ciel me tombe sur la tête"
# str2 = "It's blue"
# pos_ciel = var.find("ciel")
# print(pos_ciel)

# if "ciel" in var: 
#   print("Trouvé")

# if var.find("ciel") != -1:
#   print("Trouvé")
# pos = var.find("ciel")
# if pos != -1:
# 	print("Trouvé en position "+ str(pos))
# a = 2.1
# b = 6
# result = a + b
# print("Bonjour, bienvenue"),
# print("Le résultat de l'opération " + str(a) + " + " +str(b) + " est " + str(result))
# print("le résultat de", a, "+", b, "donne", result)
# print(f"le résultat de {a} + {b} donne {result}")

# NameList = ("John", "Mark", "Luke", "Mathieu", "Levi") 
# NmList = "\n ".join(NameList)
# print(NmList)

# var = "Le ciel me tombe sur la tête"
# str2 = "It's blue"
# pos_ciel = var.find("ciel")
# print(pos_ciel)

# if "ciel" in var: 
#   print("Trouvé")

# if var.find("ciel") != -1:
#   print("Trouvé")
# pos = var.find("ciel")
# if pos != -1:
# 	print("Trouvé en position "+ str(pos))



# var = "Hello World"

# listchars = list(str)
# print(list(str))

# malistedechar=list(str)
# sep="."
# print(sep.join(malistedechar))

# print("-----------------------")
# print(".".join(list(str)))

# var = input("Hello, je suis dans un input ")
# print ('Enter your name')
# x = input()
# print('Hello, ' + x)

# y = input('Enter where you from:')
# print ('So you are from, ' + y)

# var = "Hello World"

# listchars = list(var)

# print(str(type(var)))
# print(str(type(listchars)))
# print(str(type(listchars[0])))
# listchars.sort()
# listchars=list(var)
# list=var.split('0')
# print(listchars)
# print(len(list))

# nbr = input('Entrez un nombre entre 0 et 100:')

# if  nbr <= 100:
        #  print("Ok")
        # print("Vérifier bien que vous entrez un nombre entre 0 et 100")
   

# elif nbr < 0:
#     print("Vérifier bien que vous entrez un nombre entre 0 et 100")

# Voici la correction python if else

#!/usr/bin/env python3

# print("bonjour")
# var=int(input('Enterz un nombre entre 0 et 100:'))

# if (var >= 0) and (var <=100):
#     print(str(var) + " est bien compris entre 0 et 100")
# else:
#     print(str(var) + " n'est pas compris entre 0 et 100")

# print("au revoir")

##########################
# min=0
# max=100
# print("bonjour")
# var=int(input('Entrez un nombre entre 0 et 100:'))

# if (var >= min) and (var <= max):
#     print(str(var) + " est bien compris entre " + str(min) + " et " + str(max) )
# else:
#     print(str(var) + " n'est pas compris entre " + str(min) + " et " + str(max) )




##########################
# min=0
# max=100
# print("bonjour")
# var=int(input('Enterz un nombre entre 0 et 100:'))

# if (var >= min) :
#     print(str(var) + " est plus grand ou egal à " + str(min) )
#     if (var <= max):
#         print(str(var) + " est plus petit ou égal à " + str(max) )
#     else:
#         print(str(var) + " est plus grand que" + str(max) )
# else:
#     print(str(var) + " est plus petit que " + str(min) )

# print("au revoir")
# insrt = "A word with the letter 'a''"
# charactere = ['a', 'e', 't']
# def searchLetter(sentence, letter):
#     ListChars=list(sentence)
#     continuer = True
#     pos=0 
#     while continuer :
#         caractere_courant=ListChars[pos]
#         pos = pos + 1
#         if (caractere_courant == letter):
#             continuer = False
#         else pos >= len(ListChars):
#             continuer = False
#             pos = -1
# return pos

# for mot in MySentence.spil():
#     for t in charactere:
#         print("on cherche '" + t + "' dans le mot '" + mot + "'")
#         print(searchLetter(mot, t))
# def myfunc():
#     if not hasattr(myfunc, "var"):
#         myfunc.var = 0 # init
#     myfunc.var += 1 

#Argument par défaut
# def functionn(strr='Konoha s handsome blue beast, the name is Rock Lee', nbr1=0):
#     print(nbr1)
#     print(strr)
    
# functionn(nbr1=70)
# functionn(199, True)
# functionn(100)
# functionn(100, 200)
# functionn(strr=4)

# def functionn2(nbr2=0, nbr3=2):
#     print(nbr2)
#     print(nbr3)
    
# functionn2(nbr2=5)
# functionn2(4, 7)

# 1- Définition
# def functionn3(arg1="Bonjour"):
#     print(len(arg1))
    
# 2-Modification, total
# def functionn3(arg1):
#     if not hasattr(functionn3, "total"):
#         functionn3.total = 0
#     functionn3.total = functionn3.total + len(arg1)
#     print(functionn3.total)
   
# functionn3("Hello")
# functionn3("Halo")
# functionn3("Ohayo gozaimasu")

#Au lieu d'utiliser "return", ici on utilise "yield"// auto-générateur
# def funct():
#     print.funct()
    
#     yield "Hello"
#     yield "ça va"


# Une fonction générateur
# import random
# def functionGen(choice):
#     for n in range(choice):
#         yield random.randint(1,50)
        
# for tirage in functionGen(7):
#     print(tirage)
    
# #méthode avec for en une ligne
# seq=[random.randint(1,50) for i in range(7)]
# print(seq)

# def Prems():
#   exit(0)
# if __name__ == "__main__":
#   Prems()


#========================== fonctions sur les listes =========================== 
# coeffs=[1, 1, 3, 1]
# liste_notes_eleves= []

# for i in range (0, 2):
#     print("Inserez le nom de l'élève:")
#     Nom = input()
#     print ("entrez l'email")
#     Email = input()
#     Note = []
    
#     for n in range(0, len(coeffs)):
#       print("entrez la note " + str(n) )
#       Note.append(float(input()))
#     liste_notes_eleves.append( (Nom, Note, Email))

# for Nom, note, email in liste_notes_eleves:
  
#   liste_notes_coeffs = zip(note, coeffs)
#   somme = 0
#   somme_coeffs = 0
#   somme = sum([note*coeff for note, coeff in liste_notes_coeffs])
#   somme_coeffs = sum([ coeffs for note, coeff in liste_notes_coeffs])
#   print("MOYENNE: " + Nom + " ("+ email + ") " + str(somme/sum( coeffs)))
  
  


# mdp={}
# mdp["nyony@eecs.fr"]=hash("LAOLINA12")
# mdp["dude@eecs.fr"]=hash("LOL24")

# login=input()

# if (mdp[login] == hash(input()) ): 
#   print("success")   
# else:
#   print('wrong password')

#================ Dictionnaire en python ======================

# dictionnaire = {}
# dictionnaire["nom"] = "Bizira"
# dictionnaire["prenom"] = "Ny Ony"
# eleve = {}
# coeffs={}
# liste_notes_eleves= {}

# eleve["nom"] = "Mickaelson"
# eleve["prénom"] = "Peter"

# for i in range (0, 2):
#   print("Inserez le nom de l'élève:")
#   eleve["Nom"] = input()
#   print ("entrez l'email")
#   eleve["Email"] = input()
#   eleve["Note"] = []
    
#   for n in range(0, len(coeffs)):
#     print("entrez la note " + str(n) )
#     Note.append(float(input()))
#     liste_notes_eleves.append( (Nom, Note, Email))

# for Nom, Note, Email in liste_notes_eleves:
  
#   liste_notes_coeffs = zip(note, coeffs)
#   somme = 0
#   somme_coeffs = 0
#   somme = sum([note*coeff for note, coeff in liste_notes_coeffs])
#   somme_coeffs = sum([ coeffs for note, coeff in liste_notes_coeffs])
#   print("MOYENNE: " + Nom + " ("+ Email + ") " + str(somme/sum( coeffs)))

#======== Le code du prof ============
# eleves={}
# eleves["Marc"]= ( [12, 15, 8, 16], "marc@eecs.fr")
# eleves["Louis"]=  ( [17, 11, 8, 11], "louis@eecs.fr")
# COEFFS = [1, 1, 3, 1]

# print("-----------------------")

# for Nom in eleves:
#   LNE, Email = eleves[Nom]
#   TNC= zip(LNE, COEFFS)
#   somme = sum([ note*coeff for note, coeff in TNC])
#   somme_coeffs = sum(COEFFS)
#   print("moyenne " + Nom + " " +str(somme/somme_coeffs))
  
# print("---------------------")

# for Nom, Vals in eleves.items():
#   LNE, Email = Vals
#   TNC = zip(LNE, COEFFS)
#   somme = sum([note*coeff for note, coeff in TNC ])
#   somme_coeffs = sum(COEFFS)
#   print("moyenne " + Nom + " " +str(somme/somme_coeffs ))
  
#=================== lecture de fichiers texte ======================
#readline.py
#================== gestion des exceptions ===============

# noms= list(eleves)

# #=============== Socket ==============
# import socket

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
#   s.bind((HOST, PORT))
#   s.listen()
  
#   conn, addr = s.accept()
  
#   with conn:
#     print (f"Connected by {addr}")
#     while True:
#       data = conn.recv(1024)
#       if not data:
#         break
#       conn.sendall(data)
      
      
#Est ce que le code décrit un serveur en IPv4?
# -> Oui, 
#Est ce que le code donné décrit l'écoute de trames UDP?
# ->
#Quel protocole de haut niveau est implémet ici,
# -> Ce code ne gère aucun protocole, c'est une boîte vide qui reçois des requêtes
    
import socket
HOST = '127.0.0.1'
PORT = 3702
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
  s.bind((HOST, PORT))
  s.listen()
  
  conn, addr = s.accept()
  
  with conn:
    print (f"Connected by {addr}")
    while True:
      data = conn.recv(1234)
      print(data)
      if not data:
        break






    
    
   
    
    






