#Class for patient 

class Patient:
	
	def __init__(self, ID, Name, Diagnosis, Gender, Age):
		self.ID = ID
		self.Name = Name
		self.Diagnosis = Diagnosis
		self.Gender = Gender
		self.Age = Age

	def formatPatientInfo(self):

		return f"{self.ID}_{self.Name}_{self.Diagnosis}_{self.Gender}_{self.Age}"

	def __str__(self):
		return f"ID: {self.ID}, Name: {self.Name}, Diagnosis: {self.Diagnosis}, Gender: {self.Gender}, Age: {self.Age}"












