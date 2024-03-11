"""file that holds all global variables of the package"""
import os

BQ_DATASET = os.environ.get('BQ_DATASET')
BQ_REGION = os.environ.get('BQ_REGION')
MODEL_TARGET = os.environ.get('MODEL_TARGET')
GCP_PROJECT = os.environ.get('GCP_PROJECT')
BQ_TABLE = os.environ.get('BQ_TABLE')
