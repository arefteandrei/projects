# Este necesar să creați un șablon pentru crearea obiectelor de tip Student. Fiecare Student trebuie să aibă următoarele proprietăți:
#
# name
# address
# phone
# course
# index_number
#
# Fiecare obiect care reprezintă un student trebuie să aibă următorul comportament (metodă):
#
# getInfo()
#
# Metoda getInfo () trebuie să returneze informații cumulative despre un student ca valoare de returnare (de exemplu, Name: John Benson, address:
# High Park 36, Phone: (507) 833-3567, Course: Geography, Index number: 123/007).
#
# Ca să realizați șablonul pentru crearea obiectelor, utilizați o clasă.
#
# În final, pe baza șablonului realizat, creați trei obiecte care să reprezinte trei studenţi cu datele dorite. Peste cele trei obiecte create,
# apelați metoda de imprimare a datelor - getInfo() și afișați informațiile cu comanda print.

class Student:
    def __init__(self, name, address, phone, course, index_number):
        self.name = name
        self.address = address
        self.phone = phone
        self.course = course
        self.index_number = index_number

    def getInfo(self):
        return "Name: %s, Address: %s, Phone: %s, Course: %s, Index_no: %s" %(self.name, self.address, self.phone, self.course, self.index_number)

student1 = Student("Michael Smith", "Central Park 23", "(507) 912-3217", "History", "333/102")
student2 = Student("Conor Maynard", "88 York Road", "(020) 222-5431", "Informatics", "212/199")
student3 = Student("Pixie Lott", "9722 Queens Road", "(020) 312-8785", "Canto", "111/111")

print(student1.getInfo())
print(student2.getInfo())
print(student3.getInfo())
