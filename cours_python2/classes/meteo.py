#coding:utf-8
import pyowm

class Meteo:
    def __init__(self,apiKey):
        self.apiowm = pyowm.OWM(API_key=apiKey,language='fr')
    
    
    def afficherMeteo(self):
        print("Vous voulez la meteo de quelle pays\n")
        pays = input("Initiale du pays(Ex:US)>")
        print("Entre la ville\n")
        ville = input("Entrez le nom de la ville>")
        position = f"{ville},{pays}"
        observation =  self.apiowm.weather_at_place(position)
        meteo = observation.get_weather()
        temperature = meteo.get_temperature('celsius')['temp']
        print(f'Il fait {temperature}°C sur {ville}')
        
        
    
        