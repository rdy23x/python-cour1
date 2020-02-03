#coding:utf-8
#Import de la classe pour pouvoir l'utiliser
from cours_python_2 import GestionClient

gestclient = GestionClient()

commande = {
    1:{"name":"Ajouter un client","cmd":gestclient.ajouterclient},
    2:{"name":"Ajouter des cours au panier client","cmd":gestclient.ajoutercoursclient},
    3:{"name":"Quitter"}
    }

while True:
    print("## LISTE DES COMMANDE ##\n")
    for key,data in commande.items():
        print(f"{key} -> {data['name']}") 
    cmd = input("\nN°>")
    
    num = int(cmd)
    if not num:
        print("Commande entrer incorrect")
        continue
    if num == 3:
        print("Fin du programme")
        break
    else:
        commande[num]["cmd"]()