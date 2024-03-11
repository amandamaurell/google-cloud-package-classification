"""loads and uploads data from and to bigquery"""
from google.cloud import bigquery
import seaborn as sns
from penguin.params import *
import pandas as pd

def upload_data(penguin_df: pd.DataFrame, bq_table: str, write_mode='WRITE_TRUNCATE'):
    """
    This function uploads a dataframe to google bigquery with truncate mode.
    It creates a new table in case it doesn't exist yet.

    Parameters:
    write_mode =  'WRITE_TRUNCATE' or 'WRITE_APPEND'. If the later,
    it appends info to the pre existing table.
    """

    PROJECT = GCP_PROJECT
    DATASET = BQ_DATASET
    TABLE = bq_table

    table = f"{PROJECT}.{DATASET}.{TABLE}"

    df = penguin_df

    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(write_disposition=write_mode)

    job = client.load_table_from_dataframe(df, table, job_config=job_config)

    result = job.result()
    return f'✅ raw data saved to bigquery at {table}'
