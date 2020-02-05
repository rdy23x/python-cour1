#coding=utf-8
from googlesearch import search

def rechercheravecgoogle():
    print("Entrez votre recherche\n")
    query = input("googe>")
    for j in search(query, tld="com", num=10, stop=1, pause=2): 
        print(j) 
        
    