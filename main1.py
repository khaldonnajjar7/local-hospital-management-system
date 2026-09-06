from abc import ABC , abstractmethod
from datetime import datetime 
#------
class Person (ABC):
    def __init__(self,name= "", phone_number = int ,person_id= ""):
        self.__name = name
        self.__phone_number = phone_number 
        self.__person_id = person_id 
    @abstractmethod 
    def get_role_info(self):
        pass
    def get_name(self):
        return self.__name
    def get_phone (self):
        return self.__phone_number
    def get_person_id (self):
        return self.__person_id 
    def __str__ (self):
        return (f"name :{self.__name} , phone :{self.__phone_number} , ID :{self.__person_id}")
class Doctor (Person) :
    def __init__ (self,name, phone_number , person_id ,specialization ):
        #Forward basic person details to the parent class initializer 
        super().__init__(name, phone_number , person_id )  #it was empty because the attribute in the base class is private but know i fill it but ..>
        # to call the attribute from the super class self._Person__name or self._Person_phone_number ....

        self.__specialization  = specialization
        self.__consultation_fee = None
        self.__patients_treated = []
    def get_role_info (self) :
        n = super().get_name()
        p = super().get_phone()
        return (f"I am Doctor {n} specialize in {self.__specialization} and my phone number: {p}")
        #use to call the method or the attribute self._Person__name but it is poor practice 
    def get_specialization (self):
        return self.__specialization
    def set_consultation_fee (self,fee):
        sure = input(f"fee is :{fee} are you sure (yes,no) ?").strip().lower()
        if sure not in ("yes","y","true","i am","contiue") :
            fee = input("Enter Fee: ")
        try:
            fee = float(fee)
            if fee <= 0:
                print("Fee must be greater than zero!")
            else:
                self.__consultation_fee = fee
                print(f"Fee set successfully: {self.__consultation_fee}")
                print_fee_on_paper(self.__consultation_fee)
        except (ValueError, TypeError):
            print("Value is not a valid number!")
    def treat_patient(self,patient,record_id):
        id = record_id 
        now = datetime.now()
        time = now.strftime("%I:%M%p in %Y-%m-%d")
        key = self.__specialization 
        description = input("Enter description:  ")

        record_value = [time,description]
        record_key = key+str(id)
        record_dict = {record_key : record_value }
        
        patient.set_last_id_record(id + 1)

        if patient not in self.__patients_treated:
            self.__patients_treated.append(patient)

        patient.add_doctor(self) #the doctor as object not just his name
        print_Treatment_and_Prescription_paper(time,description,patient)
        return record_dict #the dict of record
    def get_my_patients (self):
        for p in self.__patients_treated :
            print(p.get_name()) 
    def get_specilalization(self):
        return self.__specialization 
    
class Patient (Person ):
    def __init__ (self,n,p,id ): #the dict contain Keys as specialization type (bones) + problem id (103) and the value is describtion of the problem
        super().__init__(n,p,id)
        self.__records = {}
        self.__doctors = []
        self.__last_id_record = 100 
    def get_role_info (self) :
        return (f"I am Patient {super().get_name()}")
    def add_doctor (self,doctor):
        self.__doctors.append(doctor)
    def update_records (self,new_record):
        self.__records.update(new_record)
    def print_patient_record (self):
        """ records = {
        'aa100': ['07:18PM in 2026-09-05', 'bb'],
        'kk101': ['07:18PM in 2026-09-05', 'll']  }
        """
        for k,v in self.__records.items() :
            date = v[0]
            descr = v[1]
            print(f"{k}:")
            print(f"date:{date}")
            print(f"    {descr}")
    def get_last_id_record (self):
        return self.__last_id_record 
    def set_last_id_record (self,new):
        self.__last_id_record = new 

def print_Treatment_and_Prescription_paper (time , description,patient) :
    try :
        with open("c:/kh-programing-tests/Treatment-and-Prescription.txt" , "w") as paper :
            paper.write("<<  Treatment and Prescription  >>\n")
            paper.write(f"Patient ID : {patient.get_person_id()}\n")
            paper.write(f"Name       : {patient.get_name()}\n")
            paper.write(f"Time: {time}\n")
            paper.write(f"description: \n")
            paper.write(f"    {description}\n")
    except Exception as e :
        print("\'Hi Dev!\'Error is :>",e)
def print_fee_on_paper (fee):
    with open("c:/kh-programing-tests/Treatment-and-Prescription.txt" , "a") as paper :
        paper.write(f"Fee: {str(fee)}$")
p = Patient ("khaldoon", 796,"987654")
d = Doctor("mohamed", 791, "123456","Bones")

#docotr treat patient two times 
record1 = d.treat_patient(p,p.get_last_id_record())
p.update_records(record1)
d.set_consultation_fee(input("enter consultation Fee: "))

p.print_patient_record()
