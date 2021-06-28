from dataclasses import dataclass
from datetime import datetime


@dataclass
class AdModel:
    id: int
    creation_date: datetime
    text: str
