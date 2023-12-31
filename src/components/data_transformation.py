import os
import sys
from dataclasses import dataclass
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer # used to create pipeline
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from exception import CustomException
from logger import logging

from utils import save_object


@dataclass
class DataTransformationConfig: # Gives any path/ inputs which are required

    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig() # data_transformation_config contains the info of preprocessor_obj_file_path variable

    def get_data_transformer_object(self):
        """ This function is responsible for data transformation"""
        try:
            numerical_columns = ["writing score", "reading score"]
            catagorical_columns = [
                "gender",
                "race/ethnicity",
                "parental level of education",
                "lunch",
                "test preparation course"
            ]
            # Creating pipeline
            num_pipeline = Pipeline(
                # 2 - steps
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),  # Dealing with missing values
                    ("scaler", StandardScaler()) # Doing Standard Scaling
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),  # Dealing with missing values
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )
            logging.info(f"Numerical columns: {numerical_columns}")

            logging.info(f"Catagorical columns: {catagorical_columns}")

            # for combining both the ppipelines (num_pipeline, cat_pipeline)

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline", cat_pipeline, catagorical_columns)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info(f"Read train and test data")

            logging.info(f"Obtaining preprocessing object")

            preprocessor_obj = self.get_data_transformer_object()

            target_column_name = "math score"
            numerical_columns = ["writing score", "reading score"]

            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe.")

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[ input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[ input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                # We are saving this pickle name into the hard disk
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e, sys)