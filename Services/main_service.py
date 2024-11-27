from Services.configuracion_service import get_configuracion

def main( key_configuracion : str):
    print("inicia el proceso")
    configuracion = get_configuracion(key_configuracion)
    return configuracion
    print("termina el proceso")