import json
import csv
import re
import os
import time
from datetime import datetime
from functools import wraps


# ========== DECORATORS ==========

def timing(func):
    """Decorator to measure execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"⏱️ {func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper


def log_calls(func):
    """Decorator to log function calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📞 Calling: {func.__name__} with args={args[1:]}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"✅ {func.__name__} returned: {result}")
        return result
    return wrapper


# ========== CONTEXT MANAGER ==========

class SafeFile:
    """Custom context manager for safe file operations."""

    def __init__(self, filename, mode, encoding="utf-8"):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        print(f"📂 Opening file: {self.filename} in mode {self.mode}")
        self.file = open(self.filename, self.mode, encoding=self.encoding, newline="")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"📁 Closed file: {self.filename}")
        if exc_type:
            print(f"⚠️ Exception in file operation: {exc_val}")
        return False  # propagate exceptions


# ========== CONTACT SYSTEM ==========

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
        return {"name": self.name, "phone": self.phone, "email": self.email, "address": self.address}

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"


class ContactManager:
    """Manages contacts with decorators and safe file handling."""

    def __init__(self, storage_file="contacts.json"):
        self.storage_file = storage_file
        self.contacts = []
        self.load()

    # ---------- Persistence ----------
    @timing
    @log_calls
    def load(self):
        if os.path.exists(self.storage_file):
            with SafeFile(self.storage_file, "r") as f:
                try:
                    data = json.load(f)
                    self.contacts = [Contact(**c) for c in data]
                except json.JSONDecodeError:
                    self.contacts = []
        else:
            self.contacts = []

    @timing
    @log_calls
    def save(self):
        with SafeFile(self.storage_file, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4)

    # ---------- Core Features ----------
    @log_calls
    def add_contact(self, contact):
        if self.find_contact(contact.phone) or self.find_contact(contact.email):
            raise ValueError("Duplicate contact detected")
        self.contacts.append(contact)
        self.save()

    @log_calls
    def remove_contact(self, phone):
        contact = self.find_contact(phone)
        if contact:
            self.contacts.remove(contact)
            self.save()
            return True
        return False

    @log_calls
    def find_contact(self, keyword):
        for c in self.contacts:
            if c.phone == keyword or c.email == keyword:
                return c
        return None

    @log_calls
    def search(self, keyword):
        return [
            c for c in self.contacts
            if keyword.lower() in c.name.lower()
            or keyword in c.phone
            or keyword.lower() in c.email.lower()
            or keyword.lower() in c.address.lower()
        ]

    @log_calls
    def sort_contacts(self, by="name"):
        if by not in {"name", "phone", "email"}:
            raise ValueError("Can only sort by name, phone, or email")
        self.contacts.sort(key=lambda c: getattr(c, by))

    # ---------- Import / Export ----------
    @log_calls
    def export_to_csv(self, filename="contacts.csv"):
        with SafeFile(filename, "w") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "phone", "email", "address"])
            writer.writeheader()
            for c in self.contacts:
                writer.writerow(c.to_dict())

    @log_calls
    def import_from_csv(self, filename):
        with SafeFile(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    self.add_contact(Contact(**row))
                except ValueError as e:
                    print(f"Skipping invalid/duplicate contact: {e}")

    # ---------- Backup ----------
    @timing
    @log_calls
    def backup(self):
        backup_file = f"backup_contacts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with SafeFile(backup_file, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4)
        return backup_file

    def display_all(self):
        for c in self.contacts:
            print(c)


# ========== DEMO ==========
if __name__ == "__main__":
    manager = ContactManager()

    c1 = Contact("Ajay", "1234567890", "ajay@mail.com", "Wonderland")
    c2 = Contact("Sanjay", "1987654321", "sanjay@mail.com", "Builder Street")

    try:
        manager.add_contact(c1)
        manager.add_contact(c2)
    except ValueError as e:
        print(f"⚠️ {e}")

    manager.display_all()
    manager.backup()
