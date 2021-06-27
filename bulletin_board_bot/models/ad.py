from dataclasses import dataclass
from datetime import datetime


@dataclass
class Ad:
    id: int
    creation_date: datetime
    text: str
