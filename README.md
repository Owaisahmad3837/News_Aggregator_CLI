# News Aggregator CLI

A simple Python data pipeline that collects news from **two web APIs**, validates and combines the data, removes duplicate articles, and creates a final CSV file.

## Pipeline

```text
API Source 1 ──┐
               ├──> Raw Parquet ──> Validation ──> Combine
API Source 2 ──┘                              │
                                             ↓
                                      Transform
                                             ↓
                                         Final.csv
```

## What it does

* Fetches news from two web APIs
* Stores raw data as Parquet files
* Selects and validates required columns
* Combines both sources into one dataset
* Removes duplicate articles by title
* Renames columns for the final dataset
* Exports the final data to CSV

## Project Structure

```text
News-Projects/
├── data/
│   ├── raw/
│   │   ├── source_1.parquet
│   │   └── source_2.parquet
│   ├── validation/
│   │   └── Good/
│   │       └── source.csv
│   └── Transform/
│       └── Final_data/
│           └── Final.csv
│
├── src/
│   ├── ingestion/
│   │   ├── source_1.py
│   │   └── source_2.py
│   ├── validation/
│   │   └── source.py
│   └── transform/
│       └── transform.py
│
├── test/
├── main.py
├── .env
└── README.md
```

## Technologies

* Python
* Pandas
* Requests
* Python-dotenv
* Parquet
* CSV

## Run

Create a virtual environment and install the required packages:

```bash
pip install pandas requests python-dotenv pyarrow
```

Add your API keys to `.env`:

```text
TheNewsApi=YOUR_API_KEY
GNewsApi=YOUR_API_KEY
```

Run the pipeline:

```bash
python main.py
```

The final dataset will be created at:

```text
data/Transform/Final_data/Final.csv
```

## Purpose

This project demonstrates a basic **ETL/data pipeline** workflow:

**Extract → Validate → Transform → Load**
