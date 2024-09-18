Here’s a detailed documentation for your **Advanced Phone Book Management Application** project. This includes an overview of the project, setup instructions, functionality descriptions, and sample usage. 



# Advanced Phone Book Management Application

## Project Overview

The **Phone Book Management Application** is a Python command-line program that allows users to manage a phone book. It provides functionality to add, view, search, update, and delete contacts, as well as import contacts from a CSV file. Each contact includes fields for first name, last name, phone number, email, and address. Additionally, the program includes logging to keep track of user actions.

### Key Features
- **Add, Search, Update, Delete Contacts**: Manage contacts by adding, viewing, searching, updating, and deleting them from the phone book.
- **Batch Import from CSV**: Import multiple contacts at once from a CSV file.
- **Logging**: Logs every action, including adding, updating, and deleting contacts, with timestamps.
- **Error Handling**: Handles errors like invalid file paths and missing contacts.
- **Sorting and Grouping**: Ability to sort and group contacts by first or last name (future feature).

---

## 1. Project Structure

```
PhoneBookApp/
    ├── contact.py        # Contains the Contact class that defines individual contact details
    ├── phonebook.py      # Contains the PhoneBook class that manages all the contacts
    ├── cli.py            # Command-line interface to interact with the PhoneBook class
    ├── logger.py         # Handles logging all operations to a file
    ├── phonebook.log     # The log file created to store actions and timestamps
    ├── contacts.csv      # Example CSV file for importing contacts (optional)
```


## 2. Usage

### Running the Program

1. **Open Command Prompt or Terminal**.
2. **Navigate to the project folder**:

PS C:\Users\Mohit\Desktop\phonebook>

3. **Run the program**:
   
   python cli.py
   

### Menu Options

When you run the program, you’ll be prompted with a menu that allows you to perform different operations:


### Example Operations

#### 1. Add Contact
- Follow the prompts to add a new contact.
- Input fields include First Name, Last Name, Phone, Email (optional), and Address (optional).

#### 2. Search Contacts
- Enter a name or phone number to search for a contact. Partial matches are supported.

#### 3. Update Contact
- Enter the phone number of the contact to update. You can update the first name, last name, phone, email, or address.

#### 4. Delete Contact
- Enter the phone number of the contact to delete from the phone book.

#### 5. Display All Contacts
- Lists all contacts in the phone book, with their details such as first name, last name, phone number, email, and address.

#### 6. Import from CSV
- Provide the path to a CSV file to import contacts in bulk. Ensure the CSV has the correct format: `First Name, Last Name, Phone, Email, Address`.

#### 7. Exit
- Quits the application.

---

## 4. Logging and Auditing

Every operation performed on the phone book (e.g., adding a contact, updating, or deleting) is recorded in a log file (`phonebook.log`). Each log entry includes a timestamp and a description of the action.

---

## 5. CSV Import Instructions

### CSV File Format
Ensure your CSV file follows this format (without the headers):
```csv
First Name,Last Name,Phone,Email,Address


---

## 6. Code Overview

### Contact Class (`contact.py`)

The `Contact` class represents a single contact. It contains attributes for the first name, last name, phone, email, and address. It also tracks when the contact was created and last updated.

### PhoneBook Class (`phonebook.py`)

The `PhoneBook` class manages all the contacts in the system. It supports the following operations:
- **add_contact**: Adds a new contact to the phone book.
- **batch_import**: Imports contacts from a CSV file.
- **search**: Searches for contacts by name or phone number.
- **update_contact**: Updates an existing contact by phone number.
- **delete_contact**: Deletes a contact by phone number.
- **display_contacts**: Displays all contacts in the phone book.

### Logger Class (`logger.py`)

The `Logger` class handles logging all actions to a file. Each action is recorded with a timestamp for auditing purposes.

### Command-Line Interface (`cli.py`)

The `cli.py` script provides an interactive menu for users to interact with the phone book via the command line.

---

## 7. Error Handling

### Common Errors
- **FileNotFoundError**: If a CSV file path is incorrect or the file does not exist.
- **InvalidPhoneFormat**: Ensures that phone numbers are in the format `(###) ###-####`.

### Input Validation
- The phone number is validated to ensure it matches the pattern `(###) ###-####`.
- Optional fields like email and address can be skipped by leaving them blank.

---

## 8. Future Improvements

- **Search by email or address**.
- **Sorting and grouping** contacts by various parameters (first name, last name, etc.).
- **GUI interface** to make it more user-friendly.
- **Advanced search filters** like searching by creation date or recently updated contacts.

---

## 9. Conclusion

This **Phone Book Management Application** is a robust Python project designed for beginner to intermediate developers to practice file handling, class structures, logging, and command-line interface design. It can be extended with more features as you gain more experience.

