import os

from mssql_python import connect
 
from dotenv import load_dotenv

StoredProc = """
SET NOCOUNT ON;
      EXEC dbo.InvRptGoodCardex
      @StockNo = 12,
      @CompanyNo = 1,
      @Year = 1403,
      @FDate = '14031201',
      @LDate = '14031230',
      @AG = 1,
      @AR = 1,
      @AM = 1,
      @AD = 1,
      @SSNExcSerial = 0,
      @BatchNo = '',
      @IsDraft = 1,
      @GoodCode1 = '',
      @GoodCode2 = 'zzzzzzzzzzzzzzzzzzzzzz',
      @GGM = -1,
      @unit = 0;
"""

load_dotenv()

DB_SERVER = os.getenv("DB_SERVER")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_ENCRYPT = os.getenv("DB_ENCRYPT")


def get_db_connection():

    conn_str = f"SERVER={DB_SERVER};DATABASE={DB_DATABASE};UID={DB_USERNAME};PWD={DB_PASSWORD};Encrypt={DB_ENCRYPT};"

    # Create connection object
    conn = connect(conn_str)
    return conn



def execute_stored_procedure(procedure_name: str, params: dict = None):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        if params:
            # cursor.execute(f"EXEC {procedure_name}", tuple(params.values()))
            cursor.execute(StoredProc)
        else:
            cursor.execute(StoredProc)
        
        print(cursor)
        results = []
        column_names = []
        while True:
            # Get column names from the cursor description
            if not column_names:
                column_names = [column[0] for column in cursor.description]
            
            rows = cursor.fetchall()
            if rows:
                results.extend(rows)
            if not cursor.nextset():
                break

        # Convert results into a list of dictionaries
        formatted_results = [
            dict(zip(column_names, row))
            for row in results
        ]

        return formatted_results

    except Exception as e:
        raise RuntimeError(f"Error executing our stored procedure: {str(e)}")
    finally:
        conn.close()
