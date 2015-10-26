from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class File(Base):
    __tablename__ = 'file'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    checksum = Column(String(64), nullable=False)
    folder_id = Column(Integer, ForeignKey('folder.id'))
    chunks = relationship("Chunk")


class Chunk(Base):
    __tablename__ = 'chunk'
    id = Column(Integer, primary_key=True)
    checksum = Column(String(64), nullable=False)
    file_id = Column(Integer, ForeignKey('file.id'), nullable=False)
    index_in_file = Column(Integer, nullable=False)


class Folder(Base):
    __tablename__ = 'folder'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    checksum = Column(String(64), nullable=False)
    parent_folder_id = Column(Integer, ForeignKey('folder.id'))
    files = relationship("File")

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///db_objects.sqlite')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
