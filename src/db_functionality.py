

def select(table, columns="*", where=None, orderBy=None, limit=None):

    query = f"SELECT {columns} FROM {table}"
    
    if where:
        conditions = " AND ".join([f"{k} = %s" for k in where])
        query += f" WHERE {conditions}"
        params = list(where.values())

    if orderBy:
        query += f" ORDER BY {orderBy}"
    if limit:
        query += f" LIMIT {limit}"

    return execute(query, params)


if __name__ == "__main__":

    select("Employee")
