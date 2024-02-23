from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base

username = 'user'
password = 'password'
host = 'mysql'
port = '3306'
database = 'mydatabase'

# Create the SQLAlchemy engine
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}', echo=True)

# Define the ORM model
Base = declarative_base()

class Valentine(Base):
    __tablename__ = 'valentines'
    name = Column(String(50), primary_key=True)
    message = Column(String(256))

# Create the table in the database
Base.metadata.create_all(engine)

# Create the session
Session = sessionmaker(bind=engine)
session = Session()

records = [
    {"name": "Robin", "message": "Dear Robin, Happy Valentine's Day"},
    {"name": "Alex", "message": "Dear Alex, Happy middle of February!"},
    {"name": "Jordan", "message": "Dear Jordan, Hey, what's up?"},
    {"name": "Taylor", "message": "Dear Taylor, You are cool"},
    {"name": "Casey", "message": "Dear Casey, Wishing you the best!"},
    {"name": "Jamie", "message": "Dear Jamie, What's new with you?"},
    {"name": "Morgan", "message": "Dear Morgan, Have a great day!"},
    {"name": "Frankie", "message": "Dear Frankie, You're doing great!"},
    {"name": "Jesse", "message": "Dear Jesse, Stay awesome!"},
    {"name": "Charlie", "message": "Dear Charlie, You've got this!"},
    {"name": "Sam", "message": "Dear Sam, Thinking of you today"}
]

# use Python to create the records and add them to the session
for record in records:
    new_valentine = Valentine(name=record['name'], message=record['message'])
    session.add(new_valentine)

# commit and close the session!
session.commit()
session.close()
