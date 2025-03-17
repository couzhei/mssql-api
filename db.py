import os

import pymssql
from asyncdb import AsyncDB
from dotenv import load_dotenv

StoredProc = """
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
      @unit = 0
"""

load_dotenv()

DB_SERVER = os.getenv("DB_SERVER")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")


def get_db_connection():
    # params = {
    #     "user": DB_USERNAME,
    #     "password": DB_PASSWORD,
    #     "host": DB_SERVER,
    #     "database": DB_DATABASE,
    #     "port": DB_PORT,
    #     "driver": "ODBC Driver 17 for SQL Server",
    # }
    # db = AsyncDB("mssql", params=params)
    # async with db.connection() as conn:
    #     result, error = await conn.execute("SELECT @VERSION")
    #     if error:
    #         raise RuntimeError(f"Error executing stored procedure: {error}")
    #     return conn
    conn = pymssql.connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE)
    return conn
    # cursor = conn.cursor()
    # return cursor


def execute_stored_procedure(procedure_name: str, params: dict = None):
    # conn = await get_db_connection()
    # cursor = conn.cursor(as_dict=True)
    # try:
    #     if params:
    #         # result = await conn.fetch(f"EXEC {procedure_name}", *params.values())
    #         result = cursor.execute(f"EXEC {procedure_name}", *params.values())
    #     else:
    #         # result = await conn.fetch(QUERY)
    #         result = cursor.execute(StoredProc)
    #     return result.fetchall()
    conn = get_db_connection()
    try:
        with conn.cursor(as_dict=True) as cursor:
            if params:
                cursor.callproc(procedure_name, tuple(params.values()))
            else:
                cursor.callproc(StoredProc)

            print(
                cursor.rowcount,
                cursor.description,
            )
            for row in cursor:
                print(row)
            conn.commit()
            result = cursor.fetchall()

            return result
    except Exception as e:
        raise RuntimeError(f"Error executing our stored procedure: {str(e)}")
    finally:
        conn.close()
