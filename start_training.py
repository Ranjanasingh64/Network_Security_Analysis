import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


from networksecurity.pipeline.training_pipeline import TrainingPipeline

def strat_training():
    try:
        model_training = TrainingPipeline()
        model_training.run_pipeline()
    except Exception as e:
        raise NetworkSecurityException(e, self)  


if __name__=='__main__ ':
    strat_training()