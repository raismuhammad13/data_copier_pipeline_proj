from util import get_connection


def build_insert_query(table_name, column_names):
    column_names_string = ', '.join(column_names)
    column_values = tuple(map(lambda column: column.replace(column, '%s'), column_names))
    column_values_string = ', '.join(column_values)
    query = f"""
            INSERT INTO {table_name} ({column_names_string}) VALUES ({column_values_string})
            
            """
    return query


def insert_data(connection, cursor, query, data, batch_size=100):
    recs = []
    count = 1
    for rec in data:
        # print(rec)
        recs.append(rec)
        if count % batch_size == 0:
            # print(recs)
            cursor.executemany(query, recs)
            connection.commit()
            recs = []
        count = count + 1
    print(recs)
    cursor.executemany(query, recs)
    connection.commit()


def load_table(db_details, data, column_names, table_name):
    target_db = db_details['TARGET_DB']
    connection = get_connection(db_type=target_db['DB_TYPE'],
                                server_driver=target_db['DRIVER'],
                                db_host=target_db['SERVER'],
                                db_name = target_db['DB_NAME'],
                                db_user=target_db['DB_USER'],
                                db_pass=target_db['DB_PASS']
                                )
    cursor = connection.cursor()
    query = build_insert_query(table_name, column_names)
    print("the query is: ", query)
    insert_data(connection, cursor, query, data)

    connection.close()
