import csv
from contact import Contact
from logger import Logger

class PhoneBook:
    def __init__(self):
        self.contacts = []
        self.logger = Logger()

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.logger.log(f"Added contact: {contact}")
    
    def batch_import(self, csv_file):
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 3:
                    contact = Contact(first_name=row[0], last_name=row[1], phone=row[2],
                                      email=row[3] if len(row) > 3 else None,
                                      address=row[4] if len(row) > 4 else None)
                    self.add_contact(contact)
    
    def search(self, query, field='name'):
        results = []
        for contact in self.contacts:
            if field == 'name' and (query.lower() in contact.first_name.lower() or query.lower() in contact.last_name.lower()):
                results.append(contact)
            elif field == 'phone' and query in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, old_phone, **kwargs):
        contact = self.get_contact_by_phone(old_phone)
        if contact:
            contact.update(**kwargs)
            self.logger.log(f"Updated contact: {contact}")

    def delete_contact(self, phone):
        contact = self.get_contact_by_phone(phone)
        if contact:
            self.contacts.remove(contact)
            self.logger.log(f"Deleted contact: {contact}")
    
    def get_contact_by_phone(self, phone):
        for contact in self.contacts:
            if contact.phone == phone:
                return contact
        return None
    
    def sort_contacts(self, by='last_name'):
        if by == 'first_name':
            self.contacts.sort(key=lambda contact: contact.first_name)
        else:
            self.contacts.sort(key=lambda contact: contact.last_name)

    def display_contacts(self):
     for index, contact in enumerate(self.contacts, start=1):
        print(f"Index {index}")
        print(f"  First Name: {contact.first_name}")
        print(f"  Last Name: {contact.last_name}")
        print(f"  Phone: {contact.phone}")
        print(f"  Email: {contact.email if contact.email else 'N/A'}")
        print(f"  Address: {contact.address if contact.address else 'N/A'}")
        print("-" * 30)

