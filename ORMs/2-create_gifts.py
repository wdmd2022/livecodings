from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

username = 'user'
password = 'password'
host = 'mysql'
port = '3306'
database = 'mydatabase'

# Create the SQLAlchemy engine with echo enabled for logging SQL statements
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}', echo=True)

# Define the ORM model
Base = declarative_base()

class Valentine(Base):
    __tablename__ = 'valentines'
    name = Column(String(50), primary_key=True)
    message = Column(String(256))
    gifts = relationship("Gift", backref="valentine")

class Gift(Base):
    __tablename__ = 'gifts_to_buy'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), ForeignKey('valentines.name'))
    gift = Column(String(256))

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Define the gift records
gift_records = [
    {"name": "Robin", "gift": "sculpture of us holding hands"},
    {"name": "Robin", "gift": "painting of us holding hands"},
    {"name": "Alex", "gift": "candy"},
    {"name": "Jordan", "gift": "framed poem"},
    {"name": "Taylor", "gift": "recording of song I wrote"},
    {"name": "Casey", "gift": "romantic socks"},
    {"name": "Jamie", "gift": "papier-mache heart"},
    {"name": "Morgan", "gift": "sweater"},
    {"name": "Frankie", "gift": "chocolates"},
    {"name": "Jesse", "gift": "portrait painting"},
    {"name": "Charlie", "gift": "play tickets"},
    {"name": "Sam", "gift": "flower"}
]

# Create the gift records and insert into the session
for record in gift_records:
    new_gift = Gift(name=record['name'], gift=record['gift'])
    session.add(new_gift)

# Create the table in the database
Base.metadata.create_all(engine)

# Commit and close the session
session.commit()
session.close()
