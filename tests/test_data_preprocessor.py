import pandas as pd
from src.utils.data_preprocessor import DataPreprocessor

def main():
    dataframe = pd.read_csv("data/seed/seed_roles.csv")
    processor = DataPreprocessor(dataframe)
    cleaned = processor.process()
    cleaned.to_csv("data/processed/seed_roles_clean.csv",index=False)
    print("Saved to data/processed/seed_roles_clean.csv")

if __name__ == "__main__":
    main()