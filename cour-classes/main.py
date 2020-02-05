#coding:utf-8
#Import de la classe pour pouvoir l'utiliser
from cours_python_2 import GestionClient

gestclient = GestionClient()

commande = {
    1:{"name":"Ajouter un client","cmd":gestclient.ajouterclient},
    2:{"name":"Ajouter des cours au panier client","cmd":gestclient.ajoutercoursclient},
    3:{"name":"Supprimmer client","cmd":gestclient.supprimerclient},
    4:{"name":"Supprimer un article du client","cmd":gestclient.supprimercours},
    5:{"name":"vider le panier du client","cmd":gestclient.viderpaniercours},
    7:{"name":"Quitter"}
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
    if num == 7:
        print("Fin du programme")
        break
    else:
        commande[num]["cmd"]()