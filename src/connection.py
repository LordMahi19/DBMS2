import psycopg2
from queue import Queue

class connectionPooler:

    def __init__(self, poolSize=20):
        self.pool = Queue()
        for _ in range(poolSize):
            self.pool.put(psycopg2.connect(database="bidi", user="postmanpat", password="password", host="localhost", port="5432"))

    def get(self):
        return self.pool.get()

    def release(self, connection):
        self.pool.put(connection)

    def clean(self):
        for conn in self.pool:
            conn.close()
        


def getManualDBConnection():

    connection = psycopg2.connect(database="bidi", user="postmanpat", password="password", host="localhost", port="5432")

    if connection == None:
        return -1

    print("Connection succeeded")

    cursor = connection.cursor()

    if cursor == None:
        return -1

    return connection, cursor