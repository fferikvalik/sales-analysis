
```markdown
# 📊 Sales Analysis ETL Pipeline


## Project Description
The **Sales Analysis ETL Pipeline** project is designed to process and analyze sales data using an ETL (Extract, Transform, Load) pipeline.  
Data is extracted from CSV files, cleaned using the `pandas` library, and loaded into an `SQLite` database. Analysis is performed using SQL queries.  
The project supports both a command-line interface (CLI) and a simple graphical user interface (GUI), making it accessible to different users.

## Project Structure
```bash
sales-analysis/
├── data/
│   ├── raw/               # Raw CSV data files
│   └── processed/         # Cleaned CSV data files
├── database/
│   ├── init_db.py         # Database initialization script
│   └── queries.sql        # SQL queries for analysis
├── etl/
│   ├── extract.py         # Data extraction
│   ├── transform.py       # Data cleaning and transformation
│   └── load.py            # Data loading into the database
├── desktop_app.py         # Graphical user interface
├── interface.py           # Command-line interface
├── bootstrap.py           # Project path setup
├── config.py              # Project configuration
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## How to Run the Project

### Install Dependencies
Install all required dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Prepare Data
Place your raw CSV sales data file into the `data/raw/` folder.  
Example data structure:
```csv
order_id,date,product,quantity,price,region
1001,2023-01-05,Laptop,2,999.99,Europe
1002,2023-01-06,Phone,5,699.99,Asia
```

### Using the Command-Line Interface (CLI)
The project can be managed via the command-line interface. Available commands:
```bash
python interface.py init       # Initialize the database
python interface.py extract    # Extract data from CSV
python interface.py transform  # Clean and transform data
python interface.py load       # Load cleaned data into the database
python interface.py all        # Run the full ETL process (extract, transform, load)
python interface.py reset      # Reset the database
```

### Using the Graphical User Interface (GUI)
Launch the GUI with the following command:
```bash
python desktop_app.py
```
GUI Features:
- Run individual ETL steps (extract, transform, load)
- View real-time logs
- Clear console output
- Reset the database

## Project Features
- **Full ETL Cycle**: From data extraction to loading into the database.
- **SQLite Integration**: Fast and simple database management.
- **CLI and GUI**: Two convenient ways to interact with the project.
- **Database Reset**: Easy cleanup and restart for new runs.
- **Real-Time Logging**: Track all processing steps in real time.

## Technology Stack
- **Python 3.10+**
- **pandas** — Data processing and analysis
- **SQLite3** — Data storage
- **SQLAlchemy** — Database interaction
- **Tkinter** — Graphical user interface

## Future Improvements
- **Data Visualization**: Add charts using `matplotlib` or `seaborn`.
- **Report Generation**: Create Excel or PDF reports.
- **GUI Upgrade**: Switch to `PyQt` or `customtkinter` for a modern interface.
- **Docker Support**: Containerization for easier deployment.



