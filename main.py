from database.methods import *


# add_patient("Lüke, Aladár", 33, "f")
# add_diagnose("Sifilis", "A megfázás nagyon rossz dolog")

patient = session.query(Patients).filter_by(name="Lüke, Aladár").first()
diagnose = session.query(Diagnoses).filter_by(name="Megfázás").first()


add_patient_diagnosis(patient.id, diagnose.id)
























logger.add("ConductAI.log", retention="10 days")