import pandas as pd
from config.constants import TEXT_COLUMNS

class DataPreprocessor:
    """
    Cleans and standardizes datasets before they are
    imported into the Pathfinder database.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe.copy()

    def remove_duplicates(self):
        before = len(self.dataframe)
        self.dataframe.drop_duplicates(inplace=True)
        removed = before - len(self.dataframe)
        print(f"Removed {removed} duplicate rows.")
        return self.dataframe

    def handle_missing_values(self):
        self.dataframe.fillna("", inplace=True)
        print("Missing values handled.")
        return self.dataframe

    def standardize_text(self):
        for column in TEXT_COLUMNS:
            if column in self.dataframe.columns:
                self.dataframe[column] = (
                    self.dataframe[column].astype(str).str.strip())
        print("Text standardized.")
        return self.dataframe

    def process(self):
        self.remove_duplicates()
        self.handle_missing_values()
        self.standardize_text()
        return self.dataframe