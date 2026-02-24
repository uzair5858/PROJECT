from pydantic import BaseModel, Field
from typing import Optional


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        example="Ali Choudhary",
    )
    department: Optional[str] = "general"
    salary: float = Field(..., ge=10000)
    