import os
import sys # for handling custom exception
from src.exception import CustomException
from src.logger import logging
import pandas as pd # work with df
import sklearn
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # used to create class vairables
from src.components.data_transformation import DataTransformation, DataTransformartionConfig
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig

# Ths file is Mianly to read data from a source and then to create train, test datasets

@dataclass # decorator
class DataIngestionConfig:
    # inputs to the DataIngestion Component
    train_data_path: str = os.path.join('artifacts', "train.csv") # all thre outputs are saved in artifacts folder
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # class variable which holds all three paths
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # reading data from the csv file 
            # data can be read from anywhere i.e., csv file, database, API, ...
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("read the dataset as a dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            logging.info("Train Test Split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
        
            logging.info("Ingestion of the data is completed")

            # data transfomation grabs these and then transofrms
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    
    # obj = DataIngestion()
    # obj.initiate_data_ingestion()





    # obj = DataIngestion()
    # train_data, test_data = obj.initiate_data_ingestion()

    # data_transformation = DataTransformation()
    # data_transformation.initiate_data_transformation(train_data, test_data)




    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_training(train_arr, test_arr))





