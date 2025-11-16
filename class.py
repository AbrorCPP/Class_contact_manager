import re
from re import match

nr = r"^[a-z0-9_-]{3,15}$"
pr = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
er = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"

class Contact:
    def __init__(self, name, contact,email):
        self.name = name
        self.contact = contact
        self.email = email

a = []

def add_contacts(s:list):
    while True:
        name = input("Enter your name: ")
        if not re.match(nr, name):
            break
        else:
            print("Enter a valid name.")
    while True:
        phone = input("Enter your phone number: ")
        if re.match(pr, phone):
            break
        else:
            print("Enter a valid phone number.")
    while True:
        email = input("Enter your email: ")
        if re.match(er, email):
            break
        else:
            print("Enter a valid email.")
    t = Contact(name, phone, email)
    s.append(t)

def print_contacts(s:list):
    b = 0
    for t in s:
        b+=1
        print(f"{b}.{t.name}\t {t.contact}\t {t.email}")

def edit_contacts(s:list):
    a1 = input("Enter the phone number: ")
    for t in s:
        if t.contact == a1:
            b = input("1.Username\n2.Phone\n3.Email")
            if b == "1":
                name1 = input("Enter your name: ")
                t1 = Contact(name1, t.contact,t.email)
                s.remove(t)
                s.append(t1)
            elif b == "2":
                phone2 = input("Enter your contact: ")
                t2 = Contact(t.name, phone2,t.email)
                s.remove(t)
                s.append(t2)
            elif b == "3":
                email1 = input("Enter your email: ")
                t2 = Contact(t.name, t.contact,email1)
                s.remove(t)
                s.append(t2)

def delete_contacts(s:list):
    a = input("Enter the phone number: ")
    for t in s:
        if t.contact == a:
            s.remove(t)
            print("Successfully deleted")


def main_manager(s:list):
    while True:
        a = input("1.Add contacts\n2.Print contacts\n3.Edit contacts\n4.Delete contacts\n5.Exit\n--->")
        if a == "1":
            add_contacts(s)
        elif a == "2":
            print_contacts(s)
        elif a == "3":
            edit_contacts(s)
        elif a == "4":
            delete_contacts(s)
        else:
            print("Shutdown")
            break

main_manager(a)