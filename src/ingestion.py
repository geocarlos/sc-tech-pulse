import duckdb
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def ingest_data(db_path='data/sc_entrepreneurship.duckdb', csv_path='data/raw/sc_startups_raw.csv'):
    """
    Ingests raw CSV data into a persistent DuckDB table.
    """
    if not os.path.exists(csv_path):
        logging.error(f"Raw file not found at {csv_path}. Did you run the generator?")
        return

    con = duckdb.connect(db_path)

    try:
        logging.info(f"Loading {csv_path} into DuckDB...")
        
        con.execute(f"""
            CREATE OR REPLACE TABLE raw_startups AS 
            SELECT * FROM read_csv('{csv_path}', auto_detect=True);
        """)
        
        row_count = con.execute("SELECT COUNT(*) FROM raw_startups").fetchone()[0]
        logging.info(f"Successfully ingested {row_count} rows into 'raw_startups' table.")
        
    except Exception as e:
        logging.error(f"Ingestion failed: {e}")
    finally:
        con.close()

if __name__ == "__main__":
    ingest_data()