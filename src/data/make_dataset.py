# -*- coding: utf-8 -*-
import os
import click
import pandas as pd
import sqlalchemy as sa
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
def main(input_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    load_dotenv(find_dotenv())
    eng = sa.create_engine(os.environ['DB_URI'])
    
    dat = pd.read_csv(input_filepath)
    dat.to_sql(name='raw_data', con=eng, if_exists='replace')


if __name__ == '__main__':

    main()
