from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
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

# Query the Valentines except for Robin
valentines_to_delete = session.query(Valentine).filter(Valentine.name != 'Robin').all()

# Delete the gifts associated with the Valentines except for Robin
for valentine in valentines_to_delete:
    session.query(Gift).filter(Gift.name == valentine.name).delete()

# Delete the Valentines except for Robin
for valentine in valentines_to_delete:
    session.delete(valentine)

# Commit the changes & close the session
session.commit()
session.close()
