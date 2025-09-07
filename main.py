from src.Chickdis import logger

from Chickdis.pipeline.data_ingestion_01 import DataIngestionPipeline

STAGE_NAME=" Data ingestion stage"
try:
    logger.info(f"stage {STAGE_NAME} started")
    obj=DataIngestionPipeline
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e