from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, joinedload

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
    gifts = relationship("Gift")

class Gift(Base):
    __tablename__ = 'gifts_to_buy'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), ForeignKey('valentines.name'))
    gift = Column(String(256))

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Query all records from the table and load the associated gifts
records = session.query(Valentine).options(joinedload(Valentine.gifts)).all()


# Print the queried records along with the associated gifts
for record in records:
    print(f"Name: {record.name}, Message: {record.message}")
    if record.gifts:
        print("Gift: ")
        for gift in record.gifts:
            print(f"{gift.gift}")
    print("-----------------------------------")
    print("awww yeah I'm good at valentines day")
# close the session (hey, nothing to commit!)
session.close()

