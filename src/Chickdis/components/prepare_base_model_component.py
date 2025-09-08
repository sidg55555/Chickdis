from Chickdis.entity import BaseModelConfig, DataIngestionConfig
import os
from Chickdis import logger
import urllib.request as request
from Chickdis.utils.common import get_size
from pathlib import Path
import zipfile
import tensorflow as tf

        
class PrepareBaseModel:
    def __init__(self,config:BaseModelConfig):
        self.config=config
    
    @staticmethod
    def save_model(path:Path,model:tf.keras.Model):
            model.save(path)
    
    def get_base_model(self):
        self.model=tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )
        self.save_model(path=self.config.base_model_path,model=self.model)

    @staticmethod
    def _prepare_full_model(model,classes,freeze_all,freeze_till,learning_rate):
        if freeze_all:
            for layer in model.layers:
                layer.trainable=False
        elif (freeze_till is not None) and (freeze_till>0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable=False
       # Add custom head
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(units=classes, activation="softmax")(flatten_in)

        full_model=tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )
        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            metrics=["accuracy"],
            loss=tf.keras.losses.CategoricalCrossentropy()
        )
        full_model.summary(
        )
        return full_model
    
    def update_base_model(self):
        self.full_model=self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )
        self.save_model(path=self.config.updated_model_path,model=self.full_model)

        
    