from pathlib import Path
import pandas as pd

from config.logging_config import get_logger

from src.exceptions.pipeline_exceptions import ETLError
from src.utils.validators import DatasetValidator
from src.utils.data_preprocessor import DataPreprocessor

logger = get_logger(__name__)


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

    def __init__(self, input_file, output_file):
        self.input_file = Path(input_file)
        self.output_file = Path(output_file)

    def extract(self):
        logger.info("Extracting dataset...")
        dataframe = pd.read_csv(self.input_file)
        logger.info(f"{len(dataframe)} rows loaded.")
        return dataframe

    def validate(self, dataframe):
        logger.info("Validating dataset...")
        validator = DatasetValidator(dataframe)
        validator.validate()
        logger.info("Dataset validation completed.")
        return dataframe

    def transform(self, dataframe):
        logger.info("Transforming dataset...")

        processor = DataPreprocessor(dataframe)

        dataframe = processor.remove_duplicates()
        dataframe = processor.handle_missing_values()
        dataframe = processor.standardize_text()

        logger.info("Dataset transformation completed.")
        return dataframe

    def load(self, dataframe):
        logger.info("Saving processed dataset...")

        dataframe.to_csv(self.output_file, index=False)

        logger.info(f"Processed dataset saved to: {self.output_file}")

    def run(self):
        logger.info("ETL Pipeline Started.")

        try:
            dataframe = self.extract()
            dataframe = self.validate(dataframe)
            dataframe = self.transform(dataframe)
            self.load(dataframe)

            logger.info("ETL Pipeline Finished Successfully.")

        except Exception as e:
            logger.exception("ETL Pipeline Failed.")
            raise ETLError(str(e)) from e