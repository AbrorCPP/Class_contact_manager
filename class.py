class Contact:
    def __init__(self, name, phone,id):
        self.name = name
        self.phone = phone
        self.id = id
    def __str__(self):
        return "to'g'ri print qil"

class SMS:
    def __init__(self, name, phone, massage,id):
        self.name = name
        self.phone = phone
        self.massage = massage
        self.id = id
    def __str__(self):
        return "xato"

class Main:
    def __init__(self):
        self.contacts = []
        self.massages = []

    def con_add(self):
        n = input("Enter the username: ")
        n1 = input("Enter the phone: ")
        s = Contact(n, n1,0)
        self.contacts.append(s)

    def idd_corr(self):
        t = []
        for i in range(len(self.contacts)):
            b = i+1
            s = Contact(self.contacts[b-1].name, self.contacts[b-1].phone,i)
            t.append(s)
        self.contacts.clear()
        self.contacts.append(t)

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
                t2 = SMS(c.name, t, t1,0)
                self.massages.append(t2)

    def print_sms(self):
        for m in self.massages:
            print(f"ID.{m.id}  {m.name}: {m.phone}, {m.massage}")

    def del_massages(self):
        t = int(input("Enter the id: "))
        for m in self.massages:
            if m.id == t:
                self.massages.remove(m)

    def idd_corr_sms(self):
        t = []
        for i in range(len(self.massages)):
            b = i+1
            s = SMS(self.massages[b-1].name, self.massages[b-1].phone,self.massages[b-1].massage,i)
            t.append(s)
        self.massages.clear()
        self.massages.append(t)

