# Created by Isaac Saffran 

from patient import Patient


# Reads "patients.txt" file into list of Patient Objects
	
def readPatientsFile(filename):
	# Init empty list
	patients  = []
	
	# open file for reading
	with open(filename, "r") as file:
		# read each line of file
		for line in file:
			ID, Name, Diagnosis, Gender, Age = line.strip().split("_")
			
			# create a new Patients object
			p = Patient(ID, Name, Diagnosis, Gender, Age)
			
			# add patient object to list of patients
			patients.append(p)
		
	# return list of patients
	return patients






def searchPatientById(patients, patient_id):
	# Search for patient with specified ID
	for p in patients:
		if p.ID == patient_id:
			# Return patient object if found
			return p 
	#return -1 if not found
	return -1



def editPatientInfo(patients):
	# search for patient with specified ID
		# prompt for new values
		p.ID = input("Enter Patient ID: ") 
		p.Name = input("Enter Patient name: ")
		p.Diagnosis = input("Enter Patient diagnosis: ")
		p.Gender = input("Enter Patient gender: ")
		p.Age = input("Enter patient age: ")

 
def writePatientsListToFile(patients, file_name):
	# open file and write list of patients
	with open(file_name, "w") as file:
		for p in patients:
			file.write("{}_{}_{}_{}_{}\n".format(p.ID, p.Name, p.Diagnosis, p.Age))	



def displayPatientsList(patients):
	# display header
	print("ID\tName\nDiagnosis\tGender\tAge")
	
	# display each patient
	for p in patients:
		print(f"{p.ID}\t{p.Name}\t{p.Diagnosis}\t{p.Gender}\t{p.Age}")

#Still working on this one 
# def addPatientToList()

def patientsMenu():
	
	# display menu options
	print("0 - Return to Main Menu")
	print("1 - Display patient's list")
	print("2 - Search for patient by ID")
	print("3 - Add patient")
	print("4 - Edit patient info")
        
	# accept and return user's choice
	choice = int(input("Enter option: "))
	return choice

# display patients menu and get user's choice
choice = patientsMenu()

# process user's choice
if choice == 0:
	patientsMenu()

elif choice == 1:
	# display patients list
	patients = readPatientsFile("patients.txt")
	
	# print each patient
	for p in patients:
		print(p)



elif choice == 2:
	patient_id = int(input("Enter the Patient ID: "))
	patient_list = readPatientsFile("patients.txt")
	patient = searchPatientById(patient_list, patient_id) 	
		
	if patient != -1: 
		print(patient)
	else:
		print(f"Patient with ID {patient_id} not found.")


	
elif choice == 3:
	patient_list = readPatientsFile("patients.txt")	
	patient = editPatientInfo(patient_list)		
		
elif choice == 4:
	get_it = readPatientsFile("patients.txt")
	filename = "patients.txt"
	var = writePatientsListToFile(get_it, filename)



def enterPatientInfo():
	# ask user to enter patient information
	ID = input("Enter patient ID: ")
	Name = input("Enter patient name: ")
	Diagnosis = input("Enter patient diagnosis: ")
	Gender = input("Enter patient gender: ")
	Age = input("Enter patient age: ")

	# create and return a new Patient object
	return Patient(ID, Name, Diagnosis, Gender, Age)




