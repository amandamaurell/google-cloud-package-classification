create_bq_dataset:
	@bq mk --project_id ${GCP_PROJECT} --location=${BQ_REGION} --dataset ${BQ_DATASET}

create_bq_table:
	-bq mk --sync --project_id ${GCP_PROJECT} --location=${BQ_REGION} ${BQ_DATASET}.penguin_raw
	-bq mk --sync --project_id ${GCP_PROJECT} --location=${BQ_REGION} ${BQ_DATASET}.penguin_processed
