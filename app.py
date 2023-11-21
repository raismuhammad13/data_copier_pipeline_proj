import sys
from config import DB_DETAILS
import util
from util import get_tables, load_db_data
from read import read_table


def main():
    """Program takes at least one argument"""
    env = sys.argv[1]
    db_details = DB_DETAILS[env]   # load_db_data(env)
    tables = get_tables('table_list.txt')   # Give table name that is assigned yes.
    for table in tables['table_name']:
        print('---------------------------------------')
        print(table)
        data, columns_names = read_table(db_details, table)
        print(columns_names)
        for rec in data:
            print(rec)


if __name__ == '__main__':
    main()

    
