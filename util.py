# It will contain the functions that are relevant to connection with the source database and destination databases

import pandas as pd
from mysql import connector as mc
from mysql.connector import errorcode as ec
import pyodbc
from config import DB_DETAILS


def load_db_details(env):
    return DB_DETAILS[env]
"""
DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
                'DB_TYPE': 'mysql',
                'DB_HOST': 'localhost',
                'DB_NAME': os.environ.get('SOURCE_DB'),
                'DB_USER': os.environ.get('SOURCE_DB_USER'),
                'DB_PASS': os.environ.get('SOURCE_DB_PASS')
        },
        'TARGET_DB': {
                'DRIVER': '{ODBC Driver 17 for SQL Server}',
                'SERVER': os.environ.get('TARGET_SERVER'),
                'DATABASE': os.environ.get('TARGET_DB'),
                'Trusted_Connection': os.environ.get('Trusted_Connection'),
                'DB_USER': os.environ.get('TARGET_DB_USER'),
                'DB_PASS': os.environ.get('TARGET_DB_PASS')
        }
    }
}
"""


def get_mysql_connection(db_host, db_user, db_name, db_pass):
    try:
        connection = mc.connect(user=db_user,
                                password=db_pass,
                                host=db_host,
                                database=db_name)
    except mc.Error as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials.")
        else:
            print(error)
    return connection


def get_sql_server_connection(server_driver, db_server, db_name):
    connection_string = f"DRIVER={server_driver};Server={db_server};Database={db_name};Trusted_Connection=yes;"
    connection = pyodbc.connect(connection_string)
    return connection


def get_connection(db_type, server_driver, db_host, db_name, db_user, db_pass):
    connection = None

    if db_type == 'mysql':
        connection = get_mysql_connection(db_host=db_host,
                                          db_user=db_user,
                                          db_name=db_name,
                                          db_pass=db_pass
                                          )
    if db_type == 'sql server':
        connection = get_sql_server_connection(server_driver=server_driver,
                                               db_server=db_host,
                                               db_name=db_name)
    return connection


def sql_server_connection():
    connection_string = '''
                        "Driver={SQL Server Native Client 11.0};"
                          "Server=server_name;"
                          "Database=db_name;"
                          "Trusted_Connection=yes;"
                        '''
    print(connection_string)


def get_tables(path):
    tables = pd.read_csv(path, sep=':')
    return tables.query('to_be_loaded == "yes"')
