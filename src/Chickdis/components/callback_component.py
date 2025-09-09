import time
import os
import tensorflow as tf
from Chickdis.entity import Callbacks_config


class PrepareCallbacks:
    def __init__(self,config:Callbacks_config):
        self.config=config
    
    @property
    def _create_tb_callbacks(self):
        timestamp=time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir=os.path.join(
            self.config.tensorboard_root_log_dir,f"tb-logs-at-{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    @property
    def _create_ckpt_callbacks(self):

        return tf.keras.callbacks.ModelCheckpoint(filepath=str(self.config.checkpoint_model_filepath),save_best_only=  True)
    
    def get_tb_ckpt_callbacks(self):
        return[
            self._create_tb_callbacks,self._create_ckpt_callbacks
        ]