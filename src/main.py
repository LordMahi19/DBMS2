import connection

# main should create connection pooler and start the ui, but for now i put a simple demo here

## you can use connectionpooler to get and return connections that execute queries

def main():

    connectionpool = connection.connectionPooler()

    c = connectionpool.get()
    cur = c.cursor()

    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public';
    """)

    print(cur.fetchall())

    connectionpool.release(c)

    connectionpool.clean()


main()