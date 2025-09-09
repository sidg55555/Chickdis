from Chickdis.pipeline.training_pipeline import TrainingPipeline
from src.Chickdis import logger

from Chickdis.pipeline.data_ingestion_01 import DataIngestionPipeline
from Chickdis.pipeline.prepare_base_model_02 import BaseModelPipeline

STAGE_NAME=" Data ingestion stage"
try:
    logger.info(f"stage {STAGE_NAME} started")
    obj=DataIngestionPipeline
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME=" base model preparation stage"
try:
    logger.info(f"stage {STAGE_NAME} started")
    obj=BaseModelPipeline
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME=" Training"
try:
    logger.info(f"stage {STAGE_NAME} started")
    obj=TrainingPipeline()
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e