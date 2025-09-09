from Chickdis.components.callback_component import PrepareCallbacks
from Chickdis.components.training_component import Training
from Chickdis.config.configuration import ConfigurationManager
from Chickdis.components.prepare_base_model_component import PrepareBaseModel
from Chickdis import logger


STAGE_NAME="Training Pipeline"


class TrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config= ConfigurationManager()
        prepare_callbacks_config= config.get_callback_config()
        prepare_callbacks= PrepareCallbacks(config=prepare_callbacks_config)
        callback_list= prepare_callbacks.get_tb_ckpt_callbacks()

        training_config=config.get_training_config()
        training=Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )

if __name__ == 'main':
    try:
        logger.info(f"stage {STAGE_NAME} started")
        obj=TrainingPipeline()
        obj.main()
        logger.info(f"stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e