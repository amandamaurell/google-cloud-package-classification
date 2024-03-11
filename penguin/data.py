"""loads and uploads data from and to bigquery"""
from google.cloud import bigquery
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

    job.result()
    return f'✅ raw data saved to bigquery at {table}'


def load_data(bq_table: str) -> pd.DataFrame:
    """
    This function has the purpose of querying the BQ dataset and returning a pandas DataFrame.

    Parameters:
    bq_table = Which table we query from is defined by this variable.
    """
    query = f"""
    SELECT *
    FROM {GCP_PROJECT}.{BQ_DATASET}.{bq_table}
    """

    client = bigquery.Client(project=GCP_PROJECT)
    query_job = client.query(query)
    result = query_job.result()
    df = result.to_dataframe()
    return df
