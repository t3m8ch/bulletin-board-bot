from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    creation_date: datetime
    telegram_id: int
