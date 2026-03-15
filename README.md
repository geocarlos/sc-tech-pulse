# Santa Catarina Tech Pulse: Entrepreneurship ETL and Analytics

## Project Overview

The Santa Catarina Tech Pulse is a data engineering prototype designed to demonstrate a complete ETL (Extract, Transform, Load) pipeline for regional business analytics. The project automates the processing of municipal data to generate key performance indicators such as Startup Density and Average Team Size.

### Project Scope and Data Integrity

Note on Data: This project currently utilizes synthetic (mock) data for demonstration purposes. However, the system is architected as a plug-and-play framework; real-world data from public registries can be integrated into the raw layer to produce actual geographic economic insights, hopefully with just a few or no tweaks required.

## Technical Architecture

The project uses a modular data stack to ensure clear separation between data transformation and presentation:

* Storage: DuckDB – An analytical database for high-performance, in-process queries.
* Transformation: dbt (data build tool) – Used for SQL modeling, data lineage, and schema testing.
* Presentation: Streamlit – A Python framework for building interactive data dashboards.
* Orchestration: uv – A fast Python package manager used for dependency resolution and script execution.

## Execution Instructions

### 1. Prerequisites

* **Python 3.13** (it may run with Python 3.12 or 3.14, but I have developed and tested it with Python 3.13)
* **uv** package manager.

### 2. Environment Setup

Clone the repository and install the synchronized dependencies:

```bash
git clone <repository-url>
cd sc-tech-pulse
uv sync

```

### 3. Running the Pipeline

The project can be executed in two ways:

#### Option A: One-Command Execution (Recommended)

This runs the full ETL process and prepares the data environment in a single step:

```bash
uv run main.py

```

#### Option B: Manual Step-by-Step

Components can be run individually from the root directory:

```bash
# Run mock data generator if no CSV file is in data/raw
uv run src/generator.py

# Ingest data from CSV file to DuckDB
uv run src/ingestion.py

# Run data transformations
uv run dbt build

# Launch the dashboard
cd presentation/
uv run streamlit run app.py

```

Note: Streamlit is run in a different environment because it requires a Protobuf version different from the one required by dbt, so that both can't work in the same environment.

## Data Inspection and Troubleshooting

If the Streamlit dashboard fails to load or if a quick verification of the data is required, the Gold Layer results can be inspected directly from the terminal.

### Option 1: Using dbt (No additional installation required)

If you do not have DuckDB installed as a standalone application, use dbt to preview the results:

```bash
uv run dbt show --select fct_startup_density --limit 5

```

### Option 2: Using DuckDB CLI (Cleaner output)

If you have the DuckDB standalone application installed and configured in your PATH, this option provides a cleaner, table-formatted output. Note that this may require manual environment variable setup depending on your operating system:

```bash
uv run duckdb data/sc_business_data.duckdb "SELECT startup_rank, city_name, total_startups, total_employees FROM main_main.fct_startup_density LIMIT 5;"

```

### Run tests

The tests are run with dbt and are defined in the file `models/staging/schema.yml`.

```bash
uv run dbt test
```

## Analytical Metrics

The pipeline transforms raw records into three primary metrics:

1. Total Startups: Absolute count of active technology companies per municipality.
2. Total Employees: Sum of the workforce within the specified sector and region.
3. Avg Team Size: A ratio of employees to companies, used as a proxy for regional corporate maturity.

## Future Improvements and Roadmap

The following items have been identified as strategic enhancements to move this prototype toward a production-grade analytical platform:

### 1. Integration of Empirical Data Sources

The primary objective for the next phase is to replace the current synthetic generation layer with real-world data. Potential sources include public registries and federal open data repositories to provide authentic economic insights.

### 2. Environment Toggle for Data Modes

Implement a configuration-based switch (e.g., via environment variables) to allow the system to toggle seamlessly between **Mock Mode** (for development and testing) and **Production Mode** (for real-world data ingestion) without requiring code changes.

### 3. Diversification of Input Protocols

Expand the ingestion layer to support data formats beyond local CSV files. This includes:

* Direct integration with cloud storage (Amazon S3 or Google Cloud Storage).
* Connection to external SQL databases or specialized API endpoints.

### 4. Decoupled API Service

Transition the architecture to serve data as a standalone API. By abstracting the data layer from the Streamlit presentation, the system will be able to provide insights to multiple external consumers, such as mobile applications, enterprise BI tools, or third-party web services.
