from classes import *


# Main entry Function
def main():
  while True:
    print("Welcome to the Alberta Rural Patient Care Management System\n")
    choice = mainMenu()
    if choice == 0:
      break
    elif choice == 1:
      doctorsMenu()
    elif choice == 2:
      facilitiesMenu()
    elif choice == 3:
      laboratoriesMenu()
    elif choice == 4:
      patientsMenu()
    else:
      print("Invalid choice. Please try again.\n")


"""
This Location Contains all the Doctor related Functions
"""


def enterDrInfo():
    id = input("Enter Dr ID: ")
    name = input("Enter Dr name: ")
    specialty = input("Enter Dr specialty: ")
    qualifications = input("Enter Dr qualifications: ")
    room_number = input("Enter Dr room number: ")

    new_doctor = Doctor(id, name, specialty, qualifications, room_number)

    return new_doctor

# ReadDocFile
def readDoctorsFile():
    doctors = []

    with open("doctors.txt", "r") as file:
        for line in file:
            values = line.split("_")
            doctor = Doctor(*values)
            doctors.append(doctor)

    # Print the attributes of each Doctor object in the list
    print("\n")
    return doctors

# Search Doc ID
def searchDoctorById(doctor_id, doctors):
    for doctor in doctors:
        if doctor.id == doctor_id:
            return doctor
    return -1


# Search By Name
def searchDoctorByName(doctors, search_string):
    # Iterate over the list of doctors
    for doctor in doctors:
        # Check if doctor's name matches the search string
        if doctor.name == search_string:
            # Print the doctor object if found
            return doctor
    return search_string



#edit Doc info
def editDoctorInfo(doctor_id, doctors):
    # Search for the doctor by ID
    doctor = searchDoctorById(doctor_id, doctors)

    # If the doctor was not found, return -1
    if doctor == -1:
        return -1

    # Prompt the user for the new values
    print("Enter the new values for the doctor:")
    name = input("Name: ")
    age = input("Age: ")
    specialty = input("Specialty: ")
    location = input("Location: ")

    # Update the doctor's attributes with the new values
    doctor.name = name
    doctor.age = age
    doctor.specialty = specialty
    doctor.location = location

    # Return the updated doctor
    return doctor

# This one might be junk 
def editDoctorInfo(doctorId, newName, newSpecialty, newSchedule, newQualifications, newRoomNbr):
    # read in the text file
    with open("doctors.txt", "r") as file:
        lines = file.readlines()

    # find the line with the doctorId and split it into its parts
    for i, line in enumerate(lines):
        parts = line.strip().split("_")
        if parts[0] == doctorId:
            # update the line with the new information
            lines[i] = f"{doctorId}_{newName}_{newSpecialty}_{newSchedule}_{newQualifications}_{newRoomNbr}\n"
            break

    # write the updated lines back to the file
    with open("doctors.txt", "w") as file:
        # write all the lines before the updated line
        file.writelines(lines[:i])
        # write the updated line
        file.write(lines[i])
        # write all the lines after the updated line
        file.writelines(lines[i+1:])



def displayDoctorsList(doctors):

    for doctor in doctors:
        print("\n" + doctor.id, doctor.name, doctor.specialty, doctor.schedule, doctor.qualification, doctor.room_number, sep=" ")

# Printing the updated file after being modified 
def displayDoctorsList(filepath):
    with open(filepath, "r") as file:
        for line in file:
            doctor = line.strip().split(" ")
            print("\n" + doctor.id, doctor.name, doctor.specialty, doctor.schedule, doctor.qualification, doctor.room_number, sep=" ")


#writeDoctorsListToFile

def writeDoctorsListToFile(doctors):
    # Open the file in write mode
    with open("doctors.txt", "w") as file:
        # Loop through the list of doctors
        for doctor in doctors:
            # Write the values of the doctor's attributes to the file, separated by underscores
            file.write(doctor.id, doctor.name, doctor.specialty, doctor.schedule, doctor.qualification, doctor.room_number, sep="_")



# addDrToList V2

def addDrToList(doctors):
    # Get the values for each attribute of the Doctor object
    id = input("Enter the Dr ID: ")
    name = input("Enter the Dr name: ")
    specialty = input("Enter the Dr specialty: ")
    schedule = input("Enter the Dr schedule: ")
    qualification = input("Enter Dr qualification: ")
    room_number = input("Enter Dr room number: ")

    # Create a new Doctor object with the entered attributes
    doctor = Doctor(id, name, specialty, schedule, qualification, room_number)

    # Add the new Doctor object to the list of doctors
    doctors.append(doctor)
    return doctors


def write_doctor_from_input():
    id = input("Enter Dr ID: ")
    name = input("Enter Dr name: ")
    specialty = input("Enter Dr specialty: ")
    schedule = input("Enter Dr schedule: ")
    qualifications = input("Enter Dr qualifications: ")
    room = input("Enter Dr room number: ")

    with open("doctors.txt", "a") as f:
        f.write("\n")
        f.write("{}_{}_{}_{}_{}_{}".format(id, name, specialty, schedule, qualifications, room))



def addDrToFile(doctors):
    # Open the file in write mode
    with open("doctors.txt", "w") as file:
        # Iterate over the list of doctors
        for doctor in doctors:
            # Write the attributes of the doctor to the file
            # with underscores between the values
            file.write(f"{doctor.id}_{doctor.name}_{doctor.specialty}_{doctor.schedule}_{doctor.qualification}_{doctor.room_number}\n")


"""
This Location holds all the Facility-related Functions
"""


def addFacilityToList(facility):
    Facility.append(facility)


# Reads "Facilites.txt" file into a list of Facility objects
def readFacilitiesFile():
    # List of facilities
    facilities = []

    # Open the file and read the facility names
    with open("facilities.txt", "r") as file:
        names = file.readlines()

    # Create a Facility object for each name and add it to the list of facilities
    for name in names:
        facilities.append(Facility(name.strip()))

    # Return the list of facilities
    return facilities


def displayFacilitiesList(facilities):
    for facility in facilities:
        print(facility)

# writeFacilitiesListToFile
def writeFacilitiesListToFile(facilities):
    # Open the file in write mode
    with open("facilities.txt", "w") as file:
        # Loop through the list of doctors
        for fac in facilities:
            # Write the values of the doctor's attributes to the file, separated by underscores
            file.write(fac + "\n")

# write facility from input
def write_facility_input():
    # Get the user input
    user_input = input("Enter Facility name: ")

    # Open the file in write mode
    with open('facilities.txt', 'a') as f:
        # Write the user input to the file
        f.write("\n")
        f.write(user_input)

"""
This Location holds all the Laboratory-related Functions
"""

# addLabToList
def addLabToList(laboratories):
    Laboratory.append(laboratories)


# Displays all the Laboratory information in the laboratories list
def displayLabsList(laboratories):
    for lab in laboratories:
        print(lab)


# Ask The user to enter lab name and cost then creates and returns a laboratory object

def enterLaboratoryInfo():
    # Ask the user to enter the laboratory name and cost
    name = input("Enter Lab name: ")
    cost = input("Enter Lab cost: ")

    # Create a Laboratory object with the specified name and cost
    lab = Laboratory(name, cost)

    # Return the Laboratory object
    return lab

# Read lab
def readLaboratoriesFile():
    with open("laboratories.txt", "r") as f:
        lines = f.readlines()

    labs = []
    for line in lines:
        values = line.strip().split("_")
        name = values[0]
        cost = values[1]
        lab = Laboratory(name, cost)
        labs.append(lab)

    return labs


# Write "laboratories.txt" file from the list of laboryatory objects, maintianing correct formatting
def write_laboratories_input():
    name = input("Enter Lab name: ")
    cost = input("Enter Lab Cost: ")
    with open('laboratories.txt', 'a') as f:
        # Move the file pointer to the end of the file
        f.seek(0, 2)

        # Write the new data to the file
        f.write("\n")
        f.write("{}_{}".format(name, cost))


"""
This is the location of the Patient-related Functions
"""


def readPatientsFile():
	# Init empty list
	patients  = []
	
	# open file for reading
	with open("patients.txt", "r")as file:
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


def write_patient_from_input():
    # Prompt the user for input
    id = input("\nEnter Patient ID: ")
    name = input("Enter Patient name: ")
    diagnosis = input("Enter Patient diagnosis: ")
    gender = input("Enter Patient gender: ")
    age = input("Enter Patient age: ")

    # Open the file in append mode and move the file pointer to the end of the file
    with open("patients.txt", "a") as f:
        f.seek(0, 2)

        # Write the patient information to the file
        f.write("{}_{}_{}_{}_{}\n".format(id, name, diagnosis, gender, age))


#Edits patient info into file

def editPatientInfo(patient_id,newName, newDiagnosis, newGender, newAge):
    # Read the lines in the file into a list
    with open("patients.txt", "r") as file:
        lines = file.readlines()
    
    for i, line in enumerate(lines):
        # Find the line with the patient id and split it into its parts
        parts = line.strip().split("_")
        if parts[0] == patient_id:
            # Update the line with the new information
            lines[i] = f"{patient_id}_{newName}_{newDiagnosis}_{newGender}_{newAge}\n"
            break

    # Write all of the lines back to the file, preserving the original data
    with open("patients.txt", "w") as file:
        file.writelines(lines)


# This is the area where the menu functions live  
# This is V2 of the function making it more resilent to user input. 

def mainMenu():
    # Define the main menu options
    menu_options = ["0 - Close application", "1 - Doctors", "2 - Facilities", "3 - Laboratories", "4 - Patients"]

    print("Main Menu")

    # Print each menu option on a separate line
    for option in menu_options:
        print(option)

    # Prompt the user to select a menu option
    choice = None
    while choice is None:
        try:
            # Attempt to convert the user's input to an integer
            choice = int(input("Enter option: "))
        except ValueError:
            # If the user's input cannot be converted to an integer,
            # display an error message and prompt the user again
            print("Please enter a valid integer.")

    # Return the user's choice
    return choice


# Doctors menu

def doctorsMenu():
    while True:
        # Define the doctors menu options
        menu_options = ["0 - Return to Main menu", "1 - Display Doctors list", "2 - Search for doctor by ID", "3 - Search for doctor by name", "4 - Add doctor", "5 - Edit doctor info"]

        print("\nDoctor's Menu")

        # Print each menu option on a separate line
        for option in menu_options:
             print(option)

        # Prompt the user to select a menu option
        choice = None
        while choice is None:
            try:
                choice = int(input("Enter option: "))
            except ValueError:
                print("Please Enter a valid integer.")
        
            if choice == 0:
                return
            elif choice  == 1:
                doc = readDoctorsFile()
                for doctor in doc:
                    print(doctor.id, doctor.name, doctor.specialty, doctor.schedule, doctor.qualification, doctor.room_number, sep=" ")

            elif choice == 2:
                doctors = readDoctorsFile()

                 # Ask the user to enter a doctor ID
                doctor_id = input("Enter the doctor ID: ")

                # Search for the doctor with the specified ID
                doctor = searchDoctorById(doctor_id, doctors)

                # Print the attributes of the doctor, if found
                if doctor != -1:
                    print(doctor.id, doctor.name, doctor.specialty, doctor.schedule, doctor.qualification, doctor.room_number, sep="\t\t") 
                else:
                    print(f"\nDoctor with ID {doctor_id} not found in file")
            elif choice == 3:
                search_string = input("\nEnter the doctor name: ")
                doctors = readDoctorsFile()
                doctor = searchDoctorByName(doctors, search_string)
                if doctor != search_string:
                    print(doctor.id, doctor.name, doctor.specialty, doctor.schedule, doctor.qualification, doctor.room_number, sep="\t  ") 
                else:
                    print(f"Doctor {search_string} not found in file")
            elif choice == 4:
                write_doctor_from_input()
            elif choice == 5:
                doctors = readDoctorsFile()
                doctor_id = input("Enter the doctor ID: ")
                doctor = searchDoctorById(doctor_id, doctors)
                print(doctor.id, doctor.name, doctor.specialty, doctor.schedule, doctor.qualification, doctor.room_number, sep="\t  ")
                newName = input("Enter new name: ")
                newSpecialty = input("Enter new specialty in: ")
                newSchedule = input("Enter new schedule: ")
                newQualifications = input("Enter new qualifications: ")
                newRoom = input("Enter new room number: ")
                editDoctorInfo(doctor_id, newName, newSpecialty,newSchedule, newQualifications, newRoom)
                doc = readDoctorsFile()
                for doctor in doc:
                    print(doctor.id, doctor.name, doctor.specialty, doctor.schedule, doctor.qualification, doctor.room_number, sep="  ")




# Facilites Menu

def facilitiesMenu():
    while True:
        # Define the facilities menu options
        menu_options = ["0 - Return to Main Menu", "1 - Display Facilities list", "2 - Add Facility"]

        print("\nFacility Menu")

        for option in menu_options:
                print(option)

        #Prompt the user to select a menu option
        choice = None
        while choice is None:
            try:
                choice = int(input("Enter option: "))
            except ValueError:
                print("Please Enter a valid integer.")
        
            if choice == 0:
                return
            elif choice == 1:
                # Read the facilities file and store the list of Facility objects
                facilities = readFacilitiesFile()
                print("\n")
                for facility in facilities:
                    print(facility)
            elif choice == 2:
                write_facility_input()





# Laboratories Menu

def laboratoriesMenu():
    while True:
        # Define the menu options
        menu_options = ["0 - Return to Main Menu", "1 - Display laboratories list", "2 - Add laboratory"]

        print("\nLaboratory Menu")

        # Print each menu option on a separate line
        for option in menu_options:
            print(option)

        #Prompt the user to select a menu option
        choice = None
        while choice is None:
            try:
                choice = int(input("Enter option: "))
            except ValueError:
                print("Please Enter a valid integer.")

        if choice == 0:
            return
        elif choice == 1:
            labs = readLaboratoriesFile()
            print("\n")
            for lab in labs:
                #print(lab.name, lab.cost, sep="   ")
                # Set the list of Laboratory objects
                print("{:>20} {:>10}".format(lab.name, lab.cost))
        elif choice == 2:
            print("\n")
            write_laboratories_input()
            


  # Patients Menu


def patientsMenu():
    while True:
        # Define the menu option 
        menu_options = ["0 - Return to Main Menu", "1 - Display patient's list", "2 - Search for patient by ID", "3 - Add patient", "4 - Edit patient info"] 
    
        print("\nPatient Menu")

        for option in menu_options:
            print(option)    
    
        #Prompt the user to select a menu option
        choice = None
        while choice is None:
            try:
                choice = int(input("Enter option: "))
            except ValueError:
                print("Please Enter a valid integer.")

        if choice == 0:
            return
        elif choice == 1:
            patients = readPatientsFile()
            for p in patients:
                print(p, sep="   ")
        elif choice == 2:
            patient_id = input("Enter the Patient ID: ")
            patient_list = readPatientsFile()
            patient = searchPatientById(patient_list, patient_id) 	
		
            if patient != -1: 
                print(patient)
            else:
                print(f"Patient with ID {patient_id} not in patient file.")
        elif choice == 3:
            write_patient_from_input()
        elif choice == 4:
            patient_list = readPatientsFile()
            patient_id = input("Enter the Patient ID: ")
            patient = searchPatientById(patient_list, patient_id)
            print(patient.ID, patient.Name, patient.Diagnosis, patient.Gender, patient.Age, sep="\t ")
            newName = input("Enter new Name: ")
            newDiagnosis = input("Enter new diagnosis: ")
            newGender = input("Enter new gender: ")
            newAge = input("Enter new age: ")
            editPatientInfo(patient_id, newName, newDiagnosis, newGender, newAge)
            pat = readPatientsFile()
            for patient in pat:
                print(patient.ID, patient.Name, patient.Diagnosis, patient.Gender, patient.Age, sep="\t ")





if __name__ == "__main__":
  main()

