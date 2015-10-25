from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class File(Base):
    __tablename__ = 'file'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    parent_id = Column(Integer, ForeignKey('folder.id'))
    # Using SHA256 for the checksum
    checksum = Column(String(64), nullable=False)


class Folder(Base):
    __tablename__ = 'folder'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    files = relationship("File")
    parent_id = Column(Integer, ForeignKey('folder.id'))
    # Using SHA256 for the checksum
    checksum = Column(String(64), nullable=False)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///db_objects.sqlite')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
