from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BatchID(BaseModel):
    Batch_ID: Optional[int]
    RawWeight: int
    InTime_Raw: datetime
    InTime_Wet: datetime
    OutTime_Wet: datetime
    WetWeight: int
    InTime_Dry: datetime
    OutTime_Dry: int
    Centra_ID: int
    DryWeight: int
    InTime_Powder: int
    OutTime_Powder: int
    PowderWeight: int
    Status: str
    Package_ID: int
    WeightRescale: int

class Centra(BaseModel):
    Centra_ID: Optional[int]
    CentraName: str
    CentraAddress: str
    NumberOfEmployees: int

class Delivery(BaseModel):
    Package_ID: Optional[int]
    Status: str
    InDeliveryTime: datetime
    OutDeliveryTime: datetime
    ExpeditionType: str
