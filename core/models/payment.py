from uuid import UUID
from pydantic import BaseModel


class Payment(BaseModel):
  user: int
  price: float
  idempotence_key: UUID
