from Models.redis_model import get_redis_connection as conn

def get_configuracion(key_configuracion: str):
    try:
        # Get the connection to Redis
        connection = conn()
        # Get the configuration
        configuracion = connection.get(key_configuracion)
        return configuracion
    except Exception as e:
        print(f"Error in get_configuracion: {e}")
        return None