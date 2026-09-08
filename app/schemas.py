from pydantic import BaseModel
from datetime import datetime

class URLCreate(BaseModel):
    original_url: str

class URLResponse(BaseModel):
    short_code: str
    original_url: str
    created_at: datetime
    clicks: int
    short_url: str