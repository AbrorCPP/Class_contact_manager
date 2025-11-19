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
                a2 = Contact(s, s1)
                self.contacts.remove(c)
                self.contacts.append(a2)

    def del_contact(self):
        a = input("Enter the contact: ")
        for c in self.contacts:
            if c.phone == a:
                self.contacts.remove(c)

    def idd_corr_sms(self):
        t = []
        for i in range(len(self.massages)):
            b = i+1
            s = SMS(self.massages[b-1].name, self.massages[b-1].phone,self.massages[b-1].massage,i)
            t.append(s)
        self.massages.clear()
        self.massages.append(t)

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

m1 = Main()

while True:
    a = input(" 1.Contacts\n 2.SMS\n3.Exit\n--->")
    if a == "1":
        while True:
            a1 = input("1.Add contact\n2.Print contact\n3.Edit contact\n4.Delete contact\n5.Exit\n--->")
            if a == "1":
                m1.con_add()
            elif a == "2":
                m1.con_print()
            elif a == "3":
                m1.con_edit()
            elif a == "4":
                m1.del_contact()
            else:
                break
    if a == "2":
        while True:
            m1.idd_corr_sms()
            a2 = input("1.Send SMS\n2.Delete SMS\n3.Exit\n--->")
            if a == "1":
                m1.send_sms()
            elif a == "2":
                m1.del_massages()
            else:
                break
    else:
        break