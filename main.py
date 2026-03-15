
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
        logging.info("dbt transformations completed successfully!")

        logging.info("Step 4: Launching Streamlit Dashboard...")
        try:
            subprocess.Popen(["uv", "run", "streamlit", "run", "app.py"], cwd="presentation")
            logging.info("Dashboard launched in your default browser.")
        except Exception as e:
            logging.error(f"Failed to launch Streamlit: {e}")
    else:
        logging.error(f"dbt failed: {result.stderr}")

if __name__ == "__main__":
    run_pipeline()