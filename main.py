#coding:utf-8

#declaration du dictionnaire clients
clients = {} # clients = dict()
def initialisationprogramme():
    #recuperation du nom du client
    nom_client = input("Entre le nom du client >")
    ajout_client(nom_client)


def ajout_client(client):
    clients[client] = {}
    clients[client]['name'] = client
    clients[client]['cours']= [] # clients[client]['cours']= list()

    print(f"Vous venez d'ajouter le client {clients[client]['name']},sa liste de cours est de {len(clients[client]['cours'])}")

#démarage du programme
#initialisationprogramme()
app_start = True

while app_start:
    if app_start == False:
        break
    #afficher un message de bienvenu 
    print("<< Bienvenu dans le programme de gestion de cours client >>\n")
    #affichage de liste des client dans la base
    print("<< Voici la liste des clients >>\n")
    #pour afficher la lsite des utilisateurs formater 
    # nous allons parcourir le tablea
    for key,data in clients.items():
        print(f" > client {data['name']} nombre d'article {len(data['cours'])}\n")
    # demander de choisir un utilisateur 
    choix_client = input("Entrez le client à qui vous voulez ajouter une liste de cours\n\t Nom>")
    if choix_client in list(clients.keys()):
        cours = input("veuillez entrez les cours du client>")
        clients[choix_client]['cours'].append(cours)
    else:
        print(f"l'utilisateur {choix_client} n'existe pas dans la base")
        add_validation = input("Voulez vous l'enregistrer (oui) ou (non)>")
        add_validation = str(add_validation).lower()
        if add_validation == "oui":
            ajout_client(choix_client)
            continue
        elif add_validation == "non":
            continue
        else:
            print("la valeur entre est incorrect")

    