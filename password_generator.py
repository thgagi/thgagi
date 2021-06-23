import random
import string

class Generate_Password():

    def __init__(self):
        self.password_length=int(input("How long should your Password be? "))
        self.all_letters=string.ascii_lowercase+string.ascii_uppercase
        self.password_list=[]
        self.number_list=[]

    def valid_checker(self):
        if self.password_length<8:
            checker=input("A secure Password is at least 8 digits long! \n If you want to generate an insecure Password type 'yes' \n If you want to create a secure Password type 'no' \n")
            if checker=='no':
                self.password_length=int(input("Please type a new number in:\n "))

    def random_numbers(self):
        count=0
        while count <= self.password_length:
            self.random_number=random.randint(1,9)
            self.random_number=str(self.random_number)
            self.number_list.append(self.random_number)
            count+=1


    def random_strings(self):
        count=0
        while count<=self.password_length:#diese schleife pickt solange random zahlen bis die eingegebene Passwortlänge erreicht ist
            self.password=random.choice(self.all_letters)
            self.password_list.append(self.password)
            count+=1
        
    
    def final_password(self):
        Generate_Password.valid_checker(self)
        Generate_Password.random_numbers(self)
        Generate_Password.random_strings(self)
        count=0
        self.password_list="".join(self.password_list)#splittet die liste in einen einzelnen string
        self.number_list="".join(self.number_list)
        self.final=[]
        while count<self.password_length:
            generated=random.randint(1,2)
            if generated==1:
                self.final.append(random.choice(self.password_list))
            elif generated==2:
                self.final.append(random.choice(self.number_list))
            count +=1

        self.final="".join(self.final)
        print("Your random generated Password: "+str(self.final))

Password=Generate_Password()
Password.final_password()