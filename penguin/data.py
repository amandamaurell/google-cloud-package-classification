"""loads and uploads data from and to bigquery"""
from google.cloud import bigquery
import seaborn as sns
from penguin.params import *

def upload_data(write_mode='WRITE_TRUNCATE'):
    """
    This function uploads a dataframe to google bigquery with truncate mode.
    It creates a new table in case it doesn't exist yet.

    Parameters:
    write_mode =  'WRITE_TRUNCATE' or 'WRITE_APPEND'. If the later,
    it appends info to the pre existing table.
    """

    PROJECT = GCP_PROJECT
    DATASET = BQ_DATASET
    TABLE = "penguin_raw"

    table = f"{PROJECT}.{DATASET}.{TABLE}"

    penguin_df = sns.load_dataset('penguins')

    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(write_disposition=write_mode)

    job = client.load_table_from_dataframe(penguin_df, table, job_config=job_config)

    result = job.result()
    return f'✅ raw data saved to bigquery at {table}'
