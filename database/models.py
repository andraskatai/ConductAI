
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:@localhost/ConductAI")
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
class Patients(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)
    gender = Column(String(250))



class Diagnoses(Base):
    __tablename__ = 'diagnoses'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))

class PatientDiagnosis(Base):
    __tablename__ = 'patient_diagnosis'
    patient_id = Column(Integer, ForeignKey('patients.id'), primary_key=True)
    diagnosis_id = Column(Integer, ForeignKey('diagnoses.id'), primary_key=True)


Base.metadata.create_all(engine)