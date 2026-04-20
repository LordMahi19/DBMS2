import psycopg2

def getDBConnection():

    connection = psycopg2.connect(database="bidi", user="postmanpat", password="password", host="localhost", port="5432")

    if connection == None:
        return -1

    print("Connection succeeded")

    cursor = connection.cursor()

    if cursor == None:
        return -1

    return connection, cursor