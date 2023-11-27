import os


DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
                'DRIVER': '{ODBC 17 for SQL Server}',
                'DB_TYPE': 'mysql',
                'DB_HOST': 'localhost',
                'DB_NAME': os.environ.get('SOURCE_DB'),
                'DB_USER': os.environ.get('SOURCE_DB_USER'),
                'DB_PASS': os.environ.get('SOURCE_DB_PASS')
        },
        'TARGET_DB': {
                'DB_TYPE': 'sql server',
                'DB_HOST': 'localhost',
                'DRIVER': '{ODBC Driver 17 for SQL Server}',
                'SERVER': os.environ.get('TARGET_SERVER'),
                'DB_NAME': os.environ.get('TARGET_DB'),
                'Trusted_Connection': os.environ.get('Trusted_Connection'),
                'DB_USER': os.environ.get('TARGET_DB_USER'),
                'DB_PASS': os.environ.get('SOURCE_DB_PASS')
        }
    }
}

