from sqlalchemy import Integer, Column, DateTime, func, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class AdTable(Base):
    __tablename__ = "ad"

    id = Column(Integer, primary_key=True)
    creation_date = Column(DateTime, server_default=func.now())
    text = Column(String(300), nullable=False)

    favorites_users = relationship("FavoriteTable", back_populates="ad")

    def __repr__(self):
        return f"AdTable(id={self.id!r}, " \
               f"creation_date={self.creation_date!r}, " \
               f"text={self.text!r})"


class UserTable(Base):
    __tablename__ = "user_item"  # 'user' is busy in SQL

    id = Column(Integer, primary_key=True)
    creation_date = Column(DateTime, server_default=func.now())
    telegram_id = Column(Integer, nullable=False, unique=True)

    favorites = relationship("FavoriteTable", back_populates="user")

    def __repr__(self):
        return f"UserTable(id={self.id!r}, " \
               f"creation_date={self.creation_date!r}, " \
               f"telegram_id={self.telegram_id!r})"


class FavoriteTable(Base):
    __tablename__ = "favorite"

    ad_id = Column(Integer, ForeignKey("ad.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user_item.id"), primary_key=True)
    creation_date = Column(DateTime, server_default=func.now())

    ad = relationship("AdTable")
    user = relationship("UserTable")

    def __repr__(self):
        return f"Favorite(ad_id={self.ad_id!r}, " \
               f"user_id={self.user_id!r}, " \
               f"creation_date={self.creation_date!r})"
