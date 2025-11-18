class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def __str__(self):
        return "to'g'ri print qil"

class SMS:
    def __init__(self, name, phone, massage):
        self.name = name
        self.phone = phone
        self.massage = massage
    def __str__(self):
        return "xato"

class Main:
    def __init__(self):
        self.contacts = []
        self.massages = []

    def con_add(self):
        n = input("Enter the username: ")
        n1 = input("Enter the phone: ")
        s = Contact(n, n1)
        self.contacts.append(s)

    def con_print(self):
        for c in self.contacts:
            print(f"{c.name}: {c.phone}")

    def con_edit(self):
        a = input("Enter the contact: ")
        for c in self.contacts:
            if c.phone == a:
                s = input("Enter the new username: ")
                s1 = input("Enter the new phone: ")
                a1 = Contact(s, s1)
                self.contacts.remove(c)
                self.contacts.append(a1)

    def del_contact(self):
        a = input("Enter the contact: ")
        for c in self.contacts:
            if c.phone == a:
                self.contacts.remove(c)

    def send_sms(self):
        t = input("Enter the number: ")
        for c in self.contacts:
            if c.phone == t:
                t1 = input("Enter the text: ")
                t2 = SMS(c.name, t, t1)
                self.massages.append(t2)

    def print_sms(self):
        for m in self.massages:
            print(f"{m.name}: {m.phone}, {m.massage}")

    def del_massages(self):
        for m in self.massages:

