from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class InvRptGoodCardexRequest(BaseModel):
    """Request model for the InvRptGoodCardex stored procedure"""

    StockNo: int = Field(..., description="Stock number")
    CompanyNo: int = Field(..., description="Company number")
    Year: int = Field(..., description="Year")
    FDate: str = Field(..., description="Start date in the format YYYYMMDD")
    LDate: str = Field(..., description="End date in the format YYYYMMDD")
    AG: int = Field(1, description="AG parameter")
    AR: int = Field(1, description="AR parameter")
    AM: int = Field(1, description="AM parameter")
    AD: int = Field(1, description="AD parameter")
    SSNExcSerial: int = Field(0, description="SSNExcSerial parameter")
    BatchNo: str = Field("", description="Batch number")
    IsDraft: int = Field(1, description="IsDraft parameter")
    GoodCode1: str = Field("", description="GoodCode1 parameter")
    GoodCode2: str = Field("zzzzzzzzzzzzzzzzzzzzzz", description="GoodCode2 parameter")
    GGM: int = Field(-1, description="GGM parameter")
    unit: int = Field(0, description="Unit parameter")


class StoredProcResponse(BaseModel):
    """Generic response model for stored procedure results"""

    results: List[Dict[str, Any]] = Field(
        ..., description="Results from the stored procedure"
    )
    """Generic response model for stored procedure results"""
    results: List[Dict[str, Any]] = Field(
        ..., description="Results from the stored procedure"
    )
