from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base

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

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Query and update the message for Robin's valentine
robin_valentine = session.query(Valentine).filter_by(name='Robin').first()
robin_valentine.message = "I found out recently that I love you, after a near death experience. It is still meaningful despite, my love. Ignore the circumstances. I hope you love me too. If not, please return the gifts."

# Commit the session and close it
session.commit()
session.close()
