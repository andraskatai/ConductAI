from database.models import *
from loguru import logger



def add_patient(name, age, gender):
    patient = session.query(Patients).filter_by(name=name, age=age).first()
    if patient:
        return False
    else:
        patient = Patients(name=name, age=age, gender=gender)
        session.add(patient)
        session.commit()
        logger.info(f"{name} nevü paciens hozzádva az adatbázishoz")
        return True

def add_diagnose(name, description):
    diagnose = session.query(Diagnoses).filter_by(name=name).first()
    if diagnose:
        return False
    else:
        diagnose = Diagnoses(name=name, description=description)
        session.add(diagnose)
        session.commit()
        logger.info(f"{name} nevü diagnózis hozzádva az adatbázishoz")
        return True

def add_patient_diagnosis(patient_id, diagnosis_id):
    exist = session.query(PatientDiagnosis).filter_by(patient_id=patient_id, diagnosis_id=diagnosis_id).first()
    if exist:
        logger.info(f"A diagnózis ID: {diagnosis_id} már hozzá van rendelve a pácienshez ID: {patient_id}")
        return False
    else:
        patient_diagnosis = PatientDiagnosis(
            patient_id=patient_id,
            diagnosis_id=diagnosis_id
        )
        session.add(patient_diagnosis)
        session.commit()
        logger.info(f"Az ID: {patient_id} pacienshez a {diagnosis_id} csatolva lett!")
        return True

def query_diagnoses_by_name(name):
    patient = session.query(Patients).filter_by(name=name).first()
    mikazok = session.query(PatientDiagnosis).filter_by(patient_id=patient.id).all()

    diagnozisok = []
    for i in mikazok:
        diagnozisok.append(i.diagnosis_id)

    for m in diagnozisok:
        diagnose = session.query(Diagnoses).filter_by(id=m).first()
        print(diagnose.name)

