from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserModel:
    id: int
    creation_date: datetime
    telegram_id: int
