# conexión con la base de datos mysql

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/biblioteca_system"
motor_db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=motor_db)

