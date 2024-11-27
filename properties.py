from dotenv import load_dotenv
import os

#Carga de variables de entorno
load_dotenv()


#Modulo de configuracion de propiedades
#Se definen las propiedades de la aplicacion
#Configuracion de la base de datos
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT") 

#Configuracion de la api
API_KEY = os.getenv("API_KEY")
API_KEY_NAME = os.getenv("API_KEY_NAME")