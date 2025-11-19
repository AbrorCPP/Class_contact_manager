class Contact:
    def __init__(self, name, phone, id):
        self.name = name
        self.phone = phone
        self.id = id

    def __str__(self):
        return f"{self.id}. {self.name}: {self.phone}"


class SMS:
    def __init__(self, name, phone, message, id):
        self.name = name
        self.phone = phone
        self.message = message
        self.id = id

    def __str__(self):
        return f"{self.id}. {self.name} ({self.phone}): {self.message}"


class Main:
    def __init__(self):
        self.contacts = []
        self.messages = []

    # IDlarni qayta tartiblash (0,1,2,...)
    def fix_ids_contacts(self):
        for i, c in enumerate(self.contacts):
            c.id = i

    def fix_ids_sms(self):
        for i, m in enumerate(self.messages):
            m.id = i

    # Contact qo'shish
    def con_add(self):
        name = input("Enter username: ")
        phone = input("Enter phone: ")
        self.contacts.append(Contact(name, phone, len(self.contacts)))
        print("Added!")

    # Contactlarni chiqarish
    def con_print(self):
        if not self.contacts:
            print("No contacts.")
        for c in self.contacts:
            print(c)

    # Contact tahrirlash
    def con_edit(self):
        phone = input("Enter contact phone: ")
        for c in self.contacts:
            if c.phone == phone:
                new_name = input("Enter new username: ")
                new_phone = input("Enter new phone: ")
                c.name = new_name
                c.phone = new_phone
                print("Updated!")
                return
        print("Not found!")

    # Contact o'chirish
    def del_contact(self):
        phone = input("Enter contact phone: ")
        for c in self.contacts:
            if c.phone == phone:
                self.contacts.remove(c)
                self.fix_ids_contacts()
                print("Deleted!")
                return
        print("Not found!")

    # SMS jo'natish
    def send_sms(self):
        phone = input("Enter number: ")
        for c in self.contacts:
            if c.phone == phone:
                msg = input("Enter message: ")
                self.messages.append(SMS(c.name, phone, msg, len(self.messages)))
                print("SMS sent!")
                return
        print("Contact not found!")

    # SMSlarni chiqarish
    def print_sms(self):
        if not self.messages:
            print("No SMS.")
        for m in self.messages:
            print(m)

    # SMS o'chirish
    def del_sms(self):
        sms_id = int(input("Enter SMS ID: "))
        for m in self.messages:
            if m.id == sms_id:
                self.messages.remove(m)
                self.fix_ids_sms()
                print("SMS deleted!")
                return
        print("Not found!")


m1 = Main()

while True:
    a = input("\n1. Contacts\n2. SMS\n3. Exit\n---> ")

    if a == "1":
        while True:
            a1 = input("\n1. Add contact\n2. Print contacts\n3. Edit\n4. Delete\n5. Exit\n---> ")
            if a1 == "1":
                m1.con_add()
            elif a1 == "2":
                m1.con_print()
            elif a1 == "3":
                m1.con_edit()
            elif a1 == "4":
                m1.del_contact()
            else:
                break

    elif a == "2":
        while True:
            a2 = input("\n1. Send SMS\n2. Print SMS\n3. Delete SMS\n4. Exit\n---> ")
            if a2 == "1":
                m1.send_sms()
            elif a2 == "2":
                m1.print_sms()
            elif a2 == "3":
                m1.del_sms()
            else:
                break

    else:
        break
