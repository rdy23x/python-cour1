#coding:utf-8
from classes.meteo import Meteo
mt = Meteo("ce73347ad0755cabf3e04949b88550f9")
languageDeBase = {
    'bonjour':'bonjour',
    'comment ca va': 'ca va bien et toi',
    'donne moi la météo':mt.afficherMeteo,
    'comment tu te porte':'je me porte bien et toi ca va ?'
}


def uniformString(val):
    return str(val).lower()


while True:
    conv = input("dit quelque chose>")
    #permet de convertir toutes les 
    #valeurs entrées en chaine de caractere minuscule
    conv = uniformString(conv)
    #verifier que la reponse existe dans la base
    # for language in list(languageDeBase.keys()):
    #     if conv in language:
    #         print(language)
    
    tbkeyconv = [language for language in list(languageDeBase.keys())  if conv in language ]
    if len(tbkeyconv) > 1:
        print("Que voulez-vous me dire\n")
        for index,value in enumerate(tbkeyconv):
            print(f">{index}:{value}")
        info = input("Entrez le numero de réponse>")
        info = int(info)
        if tbkeyconv[info] in list(languageDeBase.keys()):
            if type(languageDeBase[tbkeyconv[info]]) is str:
                print(f"{languageDeBase[tbkeyconv[info]]}")
            else:
                languageDeBase[tbkeyconv[info]]()
            
    else: 
        if len(tbkeyconv) == 1 and  tbkeyconv[0] in list(languageDeBase.keys()):
            if type(languageDeBase[tbkeyconv[0]]) is str:
                print(f"{languageDeBase[tbkeyconv[0]]}")
            else:
                languageDeBase[tbkeyconv[0]]()
        else:
            print("Je n'ai pas compris")
            print(f"Qu'est que je doir repondre lorsque vous me dit <{conv}>")
            resp = input("tu doi me repondre>")
            resp = uniformString(resp)
            languageDeBase[conv] = resp
            print("Merci je vien d'apprendre de nouvelle chose")