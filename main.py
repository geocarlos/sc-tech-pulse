import logging
from src.generator import generate_sc_data as generate_mock_data
from src.ingestion import ingest_data as load_to_duckdb

def run_pipeline():
    logging.info("Step 1: Generating Mock Data...")
    generate_mock_data()

    logging.info("Step 2: Ingesting into DuckDB...")
    load_to_duckdb()

    logging.info("Step 3: To be implemented...")
    # TO-DO: Trigger dbt core directly from Python
   
    logging.info("Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()