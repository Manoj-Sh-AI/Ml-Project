import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.logger import logging  # Fixed
from src.exception import CustomException

from src.components.data_ingestion import DataIngestion  # Fixed
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class TrainPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        try:
            logging.info("Starting training pipeline")

            # Step 1: Ingest data
            logging.info("Running data ingestion")
            data_ingestion = DataIngestion()
            train_path, test_path = data_ingestion.initiate_data_ingestion()

            # Step 2: Data transformation
            logging.info("Running data transformation")
            data_transformation = DataTransformation()
            train_arr, test_arr, preprocessor_path = (
                data_transformation.initiate_data_transformation(train_path, test_path)
            )

            # Step 3: Model training
            logging.info("Running model trainer")
            model_trainer = ModelTrainer()
            r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)

            logging.info(f"Training pipeline completed. R2 score: {r2_score}")
            return r2_score

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = TrainPipeline()
    obj.run_pipeline()


