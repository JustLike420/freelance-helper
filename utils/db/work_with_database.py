from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data import config
from .models import Base, User


class SqlAlchemy:
    def __init__(self):
        self.engine = create_engine(f'postgresql+psycopg2://{config.user}:{config.password}@{config.host}/{config.db}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def create_user(self, user_id, username):
        with self.Session() as session:
            user = session.query(User).filter_by(user_id=user_id).first()
            if not user:
                user = User(user_id=user_id, username=username)
                session.add(user)
                session.commit()
