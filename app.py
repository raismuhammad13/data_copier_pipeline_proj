import sys

from util import get_tables, load_db_details, get_sql_server_connection
from read import read_table
from write import load_table


def main():
    """Program takes at least one argument"""
    env = sys.argv[1]
    db_details = load_db_details(env)
    tables = get_tables('table_list.txt')   # Give table name that is assigned yes.
    for table in tables['table_name']:
        print(f'---------------Reading data for Table {table}------------------------')

        data, columns_names = read_table(db_details, table)
        print(f'---------------Loading data for Table {table}------------------------')
        load_table(db_details, data, columns_names, table)


if __name__ == '__main__':
    main()

    
