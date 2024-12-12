import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.data_transformation import DataValidation
from networksecurity.components.model_pusher import ModelPusher
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.components.model_evaluation import ModelEvaluation


from networksecurity.entity.config_entity import (
TrainingPipelineConfig,
DataIngestionConfig,
DataValidationConfig,
DataTransformationConfig,
ModelTrainerConfig,
ModelEvaluationConfig,
ModelPusherConfig

)
from networksecurity.entity.artifact_entity import (
DataIngestionArtifact,
DataValidationArtifact,
DataTransformationArtifact,
ModelTrainerArtifact,
ModelEvaluationArtifact,
ModelPusherArtifact

)

class TrainingPipeline:
    def __init__(self):
        pass
    
    
    def start_data_ingestion(self):
        try:
            self.data_inestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info('Starting data ingestion')
            data_ingestion= DataIngestion(data_ingestion_config=self.data_inestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and artifact:{data_ingestion_artifact}")
            return data_ingestion_artifact             
          
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_transformation():
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_validation():
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_model_trainer():
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_model_pusher():
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def run_pipeline():
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
