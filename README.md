# SQL Server FastAPI Application

This is a FastAPI application that connects to SQL Server and provides an API endpoint to execute the `dbo.InvRptGoodCardex` stored procedure.

## Setup and Installation

### Option 1: Local Development

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Copy `.env.example` to `.env` and update with your SQL Server credentials:
   ```
   cp .env.example .env
   ```

### Option 2: Docker Setup

1. Ensure Docker and Docker Compose are installed on your system
2. Build and start the Docker container:
   ```
   docker-compose build
   docker-compose up
   ```
3. The API will be available at `http://localhost:8087`

## Configuration

Update the `.env` file with your SQL Server connection details:

```
DB_SERVER=your_server_name
DB_DATABASE=your_database_name
DB_USERNAME=your_username
DB_PASSWORD=your_password
DB_DRIVER=ODBC Driver 17 for SQL Server
```

Note: You may need to adjust the `DB_DRIVER` value based on your installed SQL Server ODBC drivers.

## Running the Application

### Local Development

Start the FastAPI application:

```
python main.py
```

Or with uvicorn directly:

```
uvicorn main:app --reload --host 0.0.0.0 --port 8087
```

The API will be available at `http://localhost:8087`

### Docker

```
docker-compose up
```

The API will be available at `http://localhost:8087`

## API Endpoints

### GET /
Root endpoint to verify the API is running.

### POST /api/inv-rpt-good-cardex
Execute the `dbo.InvRptGoodCardex` stored procedure.

#### Request Body:
```json
{
  "StockNo": 12,
  "CompanyNo": 1,
  "Year": 1403,
  "FDate": "14031201",
  "LDate": "14031230",
  "AG": 1,
  "AR": 1,
  "AM": 1,
  "AD": 1,
  "SSNExcSerial": 0,
  "BatchNo": "",
  "IsDraft": 1,
  "GoodCode1": "",
  "GoodCode2": "zzzzzzzzzzzzzzzzzzzzzz",
  "GGM": -1,
  "unit": 0
}
```

## Swagger UI Documentation

FastAPI automatically generates interactive API documentation. Access it at:

- Swagger UI: `http://localhost:8087/docs`
- ReDoc: `http://localhost:8087/redoc`

## Docker Technical Details

This project uses:
- Python 3.13 as the base image
- uv 0.6.6 for dependency management
- asyncdb for asynchronous SQL Server connections

The Docker setup handles all the complex dependencies needed for SQL Server connectivity in a Linux environment, making it easier to deploy consistently across different environments.
