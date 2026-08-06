from src.utils.etl_pipeline import ETLPipeline


def main():

    pipeline = ETLPipeline(
        input_file="data/seed/seed_roles.csv",
        output_file="data/processed/seed_roles_clean.csv"
    )

    pipeline.run()


if __name__ == "__main__":
    main()