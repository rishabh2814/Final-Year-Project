import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String , Integer, Float, ForeignKey,Date, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# main code starts here

class Command(Base):
    __tablename__ = "commands"
    id = Column(Integer, primary_key = True)
    actions = Column(String)
    key_code = Column(Integer)
    upload_date = Column(Date)
   
class User_Command(Base):
    __tablename__ = 'input_commands'
    id = Column(Integer, primary_key = True)
    actions = Column(String)
    key_code = Column(Integer)
    uploaded_on = Column(Date)


if __name__ == "__main__":
    engine = create_engine('sqlite:///project_db.sqlite3')
    Base.metadata.create_all(engine)
    