import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd 
from sklearn.compose import ColumnTransformer  # used to create a pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler


from src.exception import CustomException
from src.logger import logging
import os 

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        """
        This Function is responsible for data transformation.
        """
        try:
            numerical_columns = ["writing_score","reading_score"]
            categorical_columns = [
                "gender"
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]
            num_pipeline = Pipeline(
                steps = [
                    ("imputer",SimpleImputer(strategy="meadian")),
                    ("scaler",StandardScaler())

                ]
            )
            cat_pipeline = Pipeline(
                steps = [
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler())
                ]
            )
            logging.info(f"Numerical columns {numerical_columns}.")
            logging.info(f"Categorical columns {categorical_columns}.")

            preprocessor = ColumnTransformer([
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipeline",cat_pipeline,categorical_columns)
            ])
            return preprocessor



        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test completed.")
            logging.info("Obtaining preprocessing object.")
            preprocessing_obj = self.get_data_transformation_object()
            target_column_name = "math_score"
            numerical_columns = ["writing_score","reading_score"]
            input_feature_train_df = train_df.drop

        except:
            pass
        

if __name__ == "__main__":
    obj = DataTransformation()
    obj.get_data_transformation_object()
            