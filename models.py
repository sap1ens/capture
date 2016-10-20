import json

import settings
from sqlalchemy import create_engine, Column, Integer, String, Text, Enum
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine(URL(**settings.DATABASE))
Session = sessionmaker(bind=engine)


class Page(Base):
    __tablename__ = 'pages'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=True)
    link = Column(Text(), nullable=False)
    name = Column(Text(), nullable=False)
    status = Column(Enum('requested', 'in_progress', 'done', name='status'), nullable=False, default='requested')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def as_json(self):
        return json.dumps(self.as_dict())


def add(page):
    session = Session()
    session.add(page)
    session.commit()

    return page


def get_all():
    session = Session()
    results = session.query(Page).all()

    return [(dict(row.as_dict())) for row in results]


def _update_status(page_id, status):
    session = Session()
    page = session.query(Page).get(page_id)
    page.status = status
    session.commit()


def mark_as_done(page_id):
    _update_status(page_id, 'done')


def mark_as_in_progress(page_id):
    _update_status(page_id, 'in_progress')


def recreate_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
