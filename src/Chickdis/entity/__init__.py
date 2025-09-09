from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class BaseModelConfig():
    root_dir: Path
    base_model_path: Path
    updated_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int

@dataclass 
class Callbacks_config:
  root_dir: Path
  tensorboard_root_log_dir: Path
  checkpoint_model_filepath: Path

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_model_path: Path
    training: Path
    params_epoch: int
    params_batch_size: int
    params_is_augmented: bool
    params_image_size: list