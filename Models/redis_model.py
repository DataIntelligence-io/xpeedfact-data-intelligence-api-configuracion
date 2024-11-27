import redis

def get_redis_connection(host='localhost', port=6379, db=0):
    try:
        connection = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)
        # Test the connection
        connection.ping()
        print("Connected to Redis")
        return connection
    except redis.ConnectionError as e:
        print(f"Could not connect to Redis: {e}")
        return None

