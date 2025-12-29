import os
import sys
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.exception import CustomException
from src.logger import logging
from components.data_transformation import DataTransformation, DataTransformationConfig
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from components.model_trainer import ModelTrainer

# in Data ingestion component there should be some inputs such as:
# * Where to save the training data?
# * Where to save the test data?
# * Where to save the raw data?
# and so on, those kind of inputs will be created by another class called "DataIngestionConfig"


@dataclass  # its a decorator used to declare the class variables by avoiding the __init__() constructor function
class DataIngestionConfig:  # Has all the INPUTS
    train_data_path: str = os.path.join(
        "artifacts", "train.csv"
    )  # train_data_path acts as an input which will save the output produced/train.csv in this path i.e "artifacts" directory
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")


class DataIngestion:  # contains required functions
    def __init__(self):
        self.ingestion_config = (
            DataIngestionConfig()
        )  # ingestion_config-> conntains the 3 inputs contained by "DataIngestionConfig" class

    def initiate_data_ingestion(self):
        # This function is use to read the data from data bases if its stored in one

        logging.info("Enter the data ingestion method or component")

        try:
            # Resolve dataset path relative to project root so script works
            project_root = Path(__file__).resolve().parents[2]
            data_file = project_root / "notebook" / "data" / "StudentsPerformance.csv"

            if not data_file.exists():
                raise FileNotFoundError(f"Dataset not found at {data_file}")

            df = pd.read_csv(
                str(data_file)
            )  # this can be changed to read from different data sources

            logging.info("Read the dataset as Dataframe")

            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True
            )
            df.to_csv(
                self.ingestion_config.raw_data_path, index=False, header=True
            )  # raw data path is saved

            logging.info("Train test split initiated")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True
            )
            test_set.to_csv(
                self.ingestion_config.test_data_path, index=False, header=True
            )

            logging.info("Ingestion of the data is Completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
        train_data, test_data
    )

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
