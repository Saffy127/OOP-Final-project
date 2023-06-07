#CLASS 1

class Doctor:
    def __init__(self, id, name, specialty, schedule, qualification, room_number):
        self.id = id
        self.name = name
        self.specialty = specialty
        self.schedule = schedule 
        self.qualification = qualification
        self.room_number = room_number
        
    def formatDrInfo(self):
        return "_".join([str(self.id), self.name, self.specialty, self.qualification, str(self.room_number)])
    
    def __str__(self):
        return f"ID {self.id}\nName {self.name}\nSpecialty {self.specialty}\nQualification {self.qualification}\nRoom Number {self.room_number}"


#CLass 2

class Facility:
    # Constructor to initialize the facility name attribute
    def __init__(self, name):
        self.name = name

    # Method to format facility information from a .txt file
    def formatFacilityInfo(self, file_name):
        # Open the file and read the facility names
        with open(file_name, "r") as file:
            facilities = file.readlines()

        # Format the facility names and return the result
        return "" + "".join(facilities)

    # Method to format facility information for printing
    def __str__(self):
        # Format the facility name and return the result
        return  self.name


#CLASS 3

class Laboratory:
    # Constructor to initialize the laboratory attributes
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    # Method to format laboratory information from a .txt file
    def formatLabInfo(self, file_name):
        # Open the file and read the laboratory information
        with open(file_name, "r") as file:
            labs = file.readlines()

        # Format the laboratory information and return the result
        return "\n".join([lab.replace(",", "_") for lab in labs])

    # Method to format laboratory information for printing
    def __str__(self):
        # Format the laboratory information and return the result
        return " {}\n {}".format(self.name, self.cost)


#Class 4 


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
		return f" {self.ID} {self.Name} {self.Diagnosis} {self.Gender} {self.Age}"

