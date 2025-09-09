from Chickdis.constants import *
from Chickdis.utils.common import read_yaml, create_directories
from Chickdis.entity import BaseModelConfig, Callbacks_config, DataIngestionConfig, TrainingConfig
import os

class ConfigurationManager:
    def __init__(self, 
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=Path(config.unzip_dir)
        )
        return data_ingestion_config
    
    def get_base_model_config(self) -> BaseModelConfig:
        config = self.config.prepare_base_model
        params= self.params
        create_directories([config.root_dir])
        base_model_config = BaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_model_path=Path(config.base_model_updated_path),
            params_image_size= params.IMAGE_SIZE,
            params_learning_rate= params.LEARNING_RATE,
            params_include_top=params.INCLUDE_TOP,
            params_weights=params.WEIGHTS,
            params_classes=params.CLASSES
        )
        
        return base_model_config
    def get_callback_config(self):
        config=self.config.prepare_callbacks
        create_directories([Path(config.checkpoint_model_filepath),Path(config.tensorboard_root_log_dir)])
        prepare_callback_config=Callbacks_config(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath= Path(config.checkpoint_model_filepath)
        )
        return prepare_callback_config
    
    def get_training_config(self):
        config_training=self.config.training
        prepare_base_model=self.config.prepare_base_model
        
        params=self.params
        training_data=os.path.join(self.config.data_ingestion.unzip_dir,"Chicken-fecal-images")
        create_directories([Path(config_training.root_dir)])
        training_config=TrainingConfig(
                root_dir= Path(config_training.root_dir),
                trained_model_path= Path(config_training.trained_model_path),
                updated_model_path= Path(prepare_base_model.base_model_updated_path),
                training= Path(training_data),
                params_epoch= int(params.EPOCHS),
                params_batch_size= int(params.BATCH_SIZE),
                params_is_augmented= params.AUGMENTATION,
                params_image_size= params.IMAGE_SIZE

        )
        return training_config