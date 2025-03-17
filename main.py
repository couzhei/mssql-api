from typing import Any, Dict, List

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from db import execute_stored_procedure, get_db_connection
from models import InvRptGoodCardexRequest, StoredProcResponse

app = FastAPI(
    title="SQL Server API",
    description="FastAPI application to interact with SQL Server stored procedures",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Modify in production to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint to verify the API is running"""
    return {"message": "SQL Server API is running"}


@app.post("/api/inv-rpt-good-cardex", response_model=StoredProcResponse)
async def inv_rpt_good_cardex(request: InvRptGoodCardexRequest):
    """
    Execute the InvRptGoodCardex stored procedure with the provided parameters
    """
    try:
        # Convert Pydantic model to dictionary
        params = request.dict()

        # Execute the stored procedure with await
        results = execute_stored_procedure(
            procedure_name="dbo.InvRptGoodCardex", params=params
        )

        print(results)

        return {"results": results}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error executing stored procedure: {str(e)}"
        )


@app.get("/api/check-db-connection")
async def check_db_connection():
    """
    Check if the database connection is working
    """
    try:
        # Execute a simple query to verify connection
        # result = await get_db_connection()
        result = get_db_connection()
        print(result)
        return {"status": "success", "message": "Database connection is working"}
    except Exception as e:
        return {"status": "error", "message": f"Database connection error: {str(e)}"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8087)
