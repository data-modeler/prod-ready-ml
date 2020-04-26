# -*- coding: utf-8 -*-
'''
    Make Dataset
    ------------
    Creates the database tables from csv files to be used in training.
'''
import os
import sys
import pandas as pd
import sqlalchemy as sa
from dotenv import find_dotenv, load_dotenv


def load_data_to_db(input_filepath: str) -> None:
    """ Creates database table(s) from raw data.

    Note:
        The database uri should be in the environment as `DB_URI`. See the
        `.env_example` for an example of how to structure the `.env` file.

    Args:
        input_filepath: The directory of the raw csv files to be loaded into
            the database.

    Returns:
        None
    """
    load_dotenv(find_dotenv())
    eng = sa.create_engine(os.environ['DB_URI'])

    fs = os.listdir(input_filepath)
    fs = [f for f in fs if f[0] != '.']

    for f in fs:
        dat = pd.read_csv(os.path.join(input_filepath, f))
        tab_nm = f.replace('.csv', '')
        dat.to_sql(name=tab_nm, con=eng, if_exists='replace')


if __name__ == '__main__':

    load_data_to_db(input_filepath=sys.argv[1])
