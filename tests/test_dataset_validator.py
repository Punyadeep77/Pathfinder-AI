import pandas as pd

from src.utils.validators import DatasetValidator


def main():

    df = pd.read_csv("data/seed/seed_roles.csv")

    validator = DatasetValidator(df)

    validator.validate()


if __name__ == "__main__":
    main()