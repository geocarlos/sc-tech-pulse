
import subprocess
import logging
from src.generator import generate_sc_data as generate_mock_data
from src.ingestion import ingest_data as load_to_duckdb

def run_pipeline():
    logging.info("Step 1: Generating Mock Data...")
    generate_mock_data()

    logging.info("Step 2: Ingesting into DuckDB...")
    load_to_duckdb()

    logging.info("Step 3: Running dbt Transformations...")
   
    result = subprocess.run(["dbt", "build"], capture_output=True, text=True)
    
    if result.returncode == 0:
        logging.info("Pipeline completed successfully!")
    else:
        logging.error(f"dbt failed: {result.stderr}")

if __name__ == "__main__":
    run_pipeline()