from Chickdis.config.configuration import ConfigurationManager
from Chickdis.components.prepare_base_model_component import PrepareBaseModel
from Chickdis import logger


STAGE_NAME="Data ingestion stage"


class BaseModelPipeline:
    def __init__(self):
        pass
    def main():
        config_manager=ConfigurationManager()
        prepare_model_config=config_manager.get_base_model_config()
        base_model=PrepareBaseModel(prepare_model_config)
        base_model.get_base_model()
        base_model.update_base_model()

if __name__=='main':
    try:
        logger.info(f"stage {STAGE_NAME} started")
        obj=BaseModelPipeline()
        obj.main()
        logger.info(f"stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e