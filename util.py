# It will contain the functions that are relevant to connection with the source database and destination databases

import pandas as pd


def get_tables(path):
    tables = pd.read_csv(path, sep=':')
    return tables.query('to_be_loaded == "yes"')