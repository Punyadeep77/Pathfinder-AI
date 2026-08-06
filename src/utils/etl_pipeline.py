from pathlib import Path
import pandas as pd

from src.utils.validators import DatasetValidator
from src.utils.data_preprocessor import DataPreprocessor

class ETLPipeline:
    """
    Runs the complete ETL pipeline.
    Extract
        ↓
    Validate
        ↓
    Transform
        ↓
    Load
    """

    def __init__(self,input_file,output_file):

        self.input_file = Path(input_file)
        self.output_file = Path(output_file)

    def extract(self):
        print("Extracting dataset...")
        dataframe = pd.read_csv(self.input_file)
        print(f"{len(dataframe)} rows loaded.")
        return dataframe

    def validate(self, dataframe):
        validator = DatasetValidator(dataframe)
        validator.validate()
        return dataframe

    def transform(self, dataframe):
        processor = DataPreprocessor(dataframe)
        dataframe = processor.remove_duplicates()
        dataframe = processor.handle_missing_values()
        dataframe = processor.standardize_text()
        return dataframe

    def load(self, dataframe):
        dataframe.to_csv(self.output_file,index=False)
        print(f"Saved to {self.output_file}")

    def run(self):
        dataframe = self.extract()
        dataframe = self.validate(dataframe)
        dataframe = self.transform(dataframe)
        self.load(dataframe)
        print("\nETL Pipeline Finished Successfully.")