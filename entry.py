from sqlalchemy import Column, Integer, String, DateTime, Float
from base import Base


class Entry(Base):

    __tablename__ = "url"

    id = Column(Integer, primary_key=True)
    url = Column(String(40), primary_key=False)

    def __init__(self, url):

        self.url = url

    def to_dict(self):
        url_dict = {"url": self.url}
        return  url_dict

    def get_url(self):
        return self.url

