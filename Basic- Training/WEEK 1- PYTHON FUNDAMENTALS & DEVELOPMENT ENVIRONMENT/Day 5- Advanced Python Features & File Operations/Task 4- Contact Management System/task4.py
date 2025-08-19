import json
import csv
import re
import os
from datetime import datetime


class Contact:
    """Represents a contact with validation."""

    def __init__(self, name, phone, email, address=""):
        self.name = self._validate_name(name)
        self.phone = self._validate_phone(phone)
        self.email = self._validate_email(email)
        self.address = address

    def _validate_name(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        return name.strip().title()

    def _validate_phone(self, phone):
        if not re.match(r"^\+?\d{7,15}$", phone):
            raise ValueError("Invalid phone number format")
        return phone

    def _validate_email(self, email):
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            raise ValueError("Invalid email format")
        return email.lower()

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
        }

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"


class ContactManager:
    """Manages contacts with persistence and utilities."""

    def __init__(self, storage_file="contacts.json"):
        self.storage_file = storage_file
        self.contacts = []
        self.load()

    # ---------- Persistence ----------
    def load(self):
        """Load contacts from JSON file"""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    self.contacts = [Contact(**c) for c in data]
                except json.JSONDecodeError:
                    self.contacts = []
        else:
            self.contacts = []

    def save(self):
        """Save contacts to JSON file"""
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4)

    # ---------- Core Features ----------
    def add_contact(self, contact):
        if self.find_contact(contact.phone) or self.find_contact(contact.email):
            raise ValueError("Duplicate contact detected")
        self.contacts.append(contact)
        self.save()

    def remove_contact(self, phone):
        contact = self.find_contact(phone)
        if contact:
            self.contacts.remove(contact)
            self.save()
            return True
        return False

    def find_contact(self, keyword):
        """Find by phone or email"""
        for c in self.contacts:
            if c.phone == keyword or c.email == keyword:
                return c
        return None

    def search(self, keyword):
        """Search by name, phone, email, or address"""
        return [
            c for c in self.contacts
            if keyword.lower() in c.name.lower()
            or keyword in c.phone
            or keyword.lower() in c.email.lower()
            or keyword.lower() in c.address.lower()
        ]

    def sort_contacts(self, by="name"):
        """Sort contacts by a field"""
        if by not in {"name", "phone", "email"}:
            raise ValueError("Can only sort by name, phone, or email")
        self.contacts.sort(key=lambda c: getattr(c, by))

    # ---------- Import / Export ----------
    def export_to_csv(self, filename="contacts.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "phone", "email", "address"])
            writer.writeheader()
            for c in self.contacts:
                writer.writerow(c.to_dict())

    def import_from_csv(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    self.add_contact(Contact(**row))
                except ValueError as e:
                    print(f"Skipping invalid/duplicate contact: {e}")

    # ---------- Backup ----------
    def backup(self):
        backup_file = f"backup_contacts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(backup_file, "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4)
        return backup_file

    def display_all(self):
        for c in self.contacts:
            print(c)


# ========== CLI for Testing ==========
if __name__ == "__main__":
    manager = ContactManager()

    while True:
        print("\n📒 Contact Management System")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display All")
        print("5. Sort Contacts")
        print("6. Export to CSV")
        print("7. Import from CSV")
        print("8. Backup Contacts")
        print("9. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                address = input("Address: ")
                c = Contact(name, phone, email, address)
                manager.add_contact(c)
                print("✅ Contact added")

            elif choice == "2":
                phone = input("Enter phone of contact to remove: ")
                if manager.remove_contact(phone):
                    print("✅ Contact removed")
                else:
                    print("❌ Contact not found")

            elif choice == "3":
                keyword = input("Search keyword: ")
                results = manager.search(keyword)
                if results:
                    for c in results:
                        print(c)
                else:
                    print("❌ No contacts found")

            elif choice == "4":
                manager.display_all()

            elif choice == "5":
                by = input("Sort by (name/phone/email): ")
                manager.sort_contacts(by)
                manager.display_all()

            elif choice == "6":
                manager.export_to_csv()
                print("✅ Exported to contacts.csv")

            elif choice == "7":
                filename = input("Enter CSV filename: ")
                manager.import_from_csv(filename)
                print("✅ Imported contacts")

            elif choice == "8":
                backup_file = manager.backup()
                print(f"✅ Backup created: {backup_file}")

            elif choice == "9":
                print("👋 Exiting...")
                break

            else:
                print("❌ Invalid choice")
        except Exception as e:
            print(f"⚠️ Error: {e}")
