import random

class MedicalProvider:
    
    def blood_type(self):
        return random.choice(["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])

    def blood_pressure(self):
        # Simulates a healthy-ish range
        systolic = random.randint(110, 140)
        diastolic = random.randint(70, 90)
        return f"{systolic}/{diastolic}"

    def icd10_diagnosis(self):
        # A small sample of medical diagnosis codes
        diagnoses = [
            {"code": "E11.9", "desc": "Type 2 diabetes mellitus without complications"},
            {"code": "I10", "desc": "Essential (primary) hypertension"},
            {"code": "J45", "desc": "Asthma"},
            {"code": "K21.9", "desc": "Gastro-esophageal reflux disease without esophagitis"}
        ]
        return random.choice(diagnoses)

    def heart_rate(self):
        # Returns a random integer between 60 and 100
        return random.randint(60, 100)