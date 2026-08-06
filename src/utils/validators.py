import pandas as pd

from config.logging_config import get_logger

from src.exceptions.validation_exceptions import (
    MissingColumnError,
    InvalidDataError,
)

from config.constants import (
    REQUIRED_ROLE_COLUMNS,
    NUMERIC_COLUMNS,
    MIN_SCORE,
    MAX_SCORE,
)

logger = get_logger(__name__)

class DatasetValidator:
    """
    Validates datasets before they enter the
    Pathfinder preprocessing pipeline.
    """
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def validate_required_columns(self):
        missing_columns = []
        for column in REQUIRED_ROLE_COLUMNS:
            if column not in self.dataframe.columns:
                missing_columns.append(column)
        if missing_columns:
            raise MissingColumnError(f"Missing columns: {missing_columns}")
        return True

    def validate_duplicate_role_ids(self):
        duplicates = self.dataframe[self.dataframe["role_id"].duplicated()]
        if not duplicates.empty:
            raise InvalidDataError("Duplicate role_id values found.")
        return True

    def validate_numeric_columns(self):
        for column in NUMERIC_COLUMNS:
            try:
                pd.to_numeric(self.dataframe[column])
            except Exception as e:
                raise InvalidDataError(f"Invalid numeric values in '{column}'.") from e
        return True

    def validate_scores(self):
        score_columns = [
            "market_demand_score",
            "competition_score",
            "growth_score",
            "automation_risk_score"
        ]

        for column in score_columns:
            if ((self.dataframe[column] < MIN_SCORE) 
                |
                (self.dataframe[column] > MAX_SCORE)).any():
                
                raise InvalidDataError(f"Invalid score range in '{column}'. "f"Allowed range: {MIN_SCORE}-{MAX_SCORE}")
        return True
    
    def validate(self):
        self.validate_required_columns()
        self.validate_duplicate_role_ids()
        self.validate_numeric_columns()
        self.validate_scores()
        logger.info("Dataset validation successful.")
        return True