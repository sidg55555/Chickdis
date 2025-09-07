from Chickdis.config.configuration import ConfigurationManager
from Chickdis.components.Data_ingestion_component import DataIngestion
from Chickdis import logger

STAGE_NAME="Data ingestion stage"


class DataIngestionPipeline:
    def __init__(self):
        pass
    def main():
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.initiate_data_ingestion()

if __name__=='main':
    try:
        logger.info(f"stage {STAGE_NAME} started")
        obj=DataIngestionPipeline
        obj.main()
        logger.info(f"stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e