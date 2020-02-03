#coding:utf-8
#importation du module random pour auto generer le code client
import random
#déclaration de la base de donnée client(Dictionnaire python)
clientDataBase = {}

class GestionClient:
    def __init__(self):
        print("### Bienvenu dans le system de gestion des cours client ##\n")
        self.listeclient()
    
    def listeclient(self):
        if len(list(clientDataBase.keys())) > 0:
            print(f"## Liste des clients NBCLIENT {len(list(clientDataBase.keys()))}##\n")
            for key,data in clientDataBase.items():
                print("CodeC\tClient\tNb_Cours\tListeC\n")
                print(f"{key}:\t{data['name']}\t{len(data['cours'])}\t {data['cours']}")
        else:
            print(f"## Liste des clients NBCLIENT {len(list(clientDataBase.keys()))}##\n")
            print("Aucun client enregistrer\n")  
        print("\n") 
    
    def ajouterclient(self):
        client_name = input("Entrez le nom du client>")
        code_client = f"#CL{random.randint(1, 9)}{random.randint(1, 9)}"
        clientDataBase[code_client] = {}
        clientDataBase[code_client]['name'] = client_name
        clientDataBase[code_client]['cours']= []

        print(f"Vous venez d'ajouter le client {clientDataBase[code_client]['name']},sa liste de cours est de {len(clientDataBase[code_client]['cours'])}\n")
        self.listeclient()
    
    def ajoutercoursclient(self):
        print("## A qui ajouter des cours ##")
        code_client = input("Entrez du code_client>")
        if code_client in list(clientDataBase.keys()):
            addcours = True
            while addcours:
                cours = input("Nom de l'article à ajouter>")
                if not cours:
                    print("valeur entrer incorrect")
                    verif = input("Voulez-vou continuer (oui) ou (nom)>")
                    if verif == "oui":
                        addcours = True
                    else:
                        addcours = False
                        break
                else:
                    clientDataBase[code_client]['cours'].append(cours)
                    print(f"#Cours bien ajouter")
                    self.listeclient()
                    verif = input("Voulez-vou continuer (oui) ou (nom)>")
                    if verif == "oui":
                        addcours = True
                    else:
                        addcours = False
                        break
                    
                   
        else:
            print(f"ce code client {code_client} n'existe pas dans la base de donnée")            
                    
    def supprimerclient(self):
        pass
    
    def supprimercours(self):
        pass
    
    def viderpaniercours(self):
        pass
    