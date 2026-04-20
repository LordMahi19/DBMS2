import connection

def main():

    conn, cur = connection.getDBConnection()

    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public';
    """)

    print(cur.fetchall())


main()