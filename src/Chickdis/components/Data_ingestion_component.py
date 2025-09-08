

from Chickdis.entity import BaseModelConfig, DataIngestionConfig
import os
from Chickdis import logger
import urllib.request as request
from Chickdis.utils.common import get_size
from pathlib import Path
import zipfile
import tensorflow as tf

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.root_dir):
            os.makedirs(self.config.root_dir, exist_ok=True)
            logger.info(f"Created directory: {self.config.root_dir}")

        logger.info(f"Downloading data from {self.config.source_URL} to {self.config.local_data_file}")
        request.urlretrieve(self.config.source_URL, self.config.local_data_file)
        logger.info(f"Downloaded file size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        logger.info(f"Extracting zip file: {self.config.local_data_file} to {self.config.unzip_dir}")
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        logger.info("Extraction completed.")

    def initiate_data_ingestion(self):
        self.download_data()
        self.extract_zip_file()
