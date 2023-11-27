from util import get_connection, get_mysql_connection


def read_table(db_details, table_name, limit=0):
    source_db = db_details['SOURCE_DB']

    connection = get_connection(db_type=source_db['DB_TYPE'],
                                server_driver=source_db['DRIVER'],
                                db_host=source_db['DB_HOST'],
                                db_name=source_db['DB_NAME'],
                                db_user=source_db['DB_USER'],
                                db_pass=source_db['DB_PASS'],
                                )
    curses = connection.cursor()
    if limit == 0:
        query = f"SELECT * FROM {table_name}"
    else:
        query = f"SELECT * FROM {table_name} LIMIT{limit}"
    curses.execute(query)
    data = curses.fetchall()
    print(data)
    columns = curses.column_names

    connection.close()

    return data, columns

