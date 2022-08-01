from sqlalchemy import BigInteger, Column, Text, Boolean, Integer, String
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, autoincrement=False, index=True)
    username = Column(String)
    keywords = Column(String, default='')
    # premium = Column(Boolean, default=False)
    # status = Column(Boolean, default=False)
    # fav_posts = relationship('Post', back_populates='user')


class FavoritePosts(Base):
    __tablename__ = 'favorite'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(Text)
    # user = relationship("User", back_populates='fav_posts')
