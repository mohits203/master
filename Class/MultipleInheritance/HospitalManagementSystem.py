class Doctor:

    def __init__(self, doctorId: int, doctorName: str, doctorSpecialization: str):
        self.doctorId = doctorId
        self.doctorName = doctorName
        self.doctorSpecialization = doctorSpecialization

    def showDoctorIndf(self):
        print(f"doctor name : {self.doctorName}\n doctor Id : {self.doctorId}\n Doctor Specialization : {self.doctorSpecialization}")

class Patient:

    def __init__(self, patientId: int, patientName: str, disease: str):
        self.patientId = patientId
        self.patientName = patientName
        self.disease = disease

    def showPatient(self):
        print(f"patient name : {self.patientName}\n patient Id : {self.patientId}\n patient disease : {self.disease}")

class MedicalReport(Doctor, Patient):

    def __init__(self, doctorId: int, doctorName: str, doctorSpecialization: str, patientId: int, patientName: str, disease: str):
        Doctor.__init__(self, doctorId, doctorName, doctorSpecialization)
        Patient.__init__(self, patientId, patientName, disease)

    def doctorInfo(self):
        self.showDoctorIndf()

    def patientInfo(self):
        self.showPatient()

doctorId = int(input("Enter Doctor id : "))
doctorName = input("Enter Doctor Name : ")
doctorSpecialization = input("Enter Doctor Specialization : ")

patientId = int(input("Enter patient id : "))
patientName = input("Enter patient name : ")
disease = input("Enter patient disease : ")

obj = MedicalReport(doctorId, doctorName, doctorSpecialization, patientId, patientName, disease)
obj.doctorInfo()
obj.patientInfo()
