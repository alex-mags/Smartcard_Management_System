# Smartcard Management System

A Python-based Smartcard Management System developed for managing customer smartcard records. The system allows users to add, amend, remove, search, and export smartcard information through a simple menu-driven interface.

## Features

- Add new smartcard records
- Amend existing smartcard details
- Remove smartcard records
- Search for smartcards using customer information
- Export records to JSON format
- SQLite database integration
- Input validation for key fields
- Simple command-line interface

## Technologies Used

- Python 3
- SQLite3
- JSON
- Flask (API version if implemented)
- Git & GitHub

## Project Structure

```

Smartcard_Management_System/
│
├── db/
│   └── database.py
│
├── operations/
│   └── card_ops.py
│
├── exports/
│   └── exported_data.json
│
├── main.py
└── README.md

```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/alex-mags/Smartcard_Management_System.git
```

### 2. Navigate to the Project Folder

```bash
cd Smartcard_Management_System
```

### 3. Run the Program

```bash
python main.py
```

## Usage

When the program starts, a menu will be displayed:

```text
--- Smartcard Customer Management System ---

1. Add Smartcard
2. Amend Smartcard
3. Remove Smartcard
4. Search Smartcards
5. Export to JSON
6. Exit
```

Select an option and follow the on-screen instructions.

## Database Fields

Each smartcard record contains:

| Field | Description |
|---------|-------------|
| Card Number | Unique smartcard identifier |
| Card Holder Name | Customer's full name |
| Date of Birth | Customer DOB |
| Address | Customer address |
| Phone Number | Contact number |
| Email Address | Customer email |
| Card Balance | Current balance on the smartcard |
| Expiry Date | Smartcard expiry date |

## Example Record

```json
{
    "card_number": "1234567890123456",
    "name": "John Smith",
    "date_of_birth": "15-04-1990",
    "address": "1 High Street, Hull",
    "phone": "07123456789",
    "email": "john.smith@email.com",
    "balance": 25.50,
    "expiry_date": "01-01-2030"
}
```

## Future Improvements

* Web interface using Flask
* User authentication
* Smartcard transaction history
* Reporting and analytics
* CSV import/export functionality
* Advanced search filters
* GUI version using Tkinter or PyQt

## Learning Outcomes

This project demonstrates:

* Database design and management
* CRUD operations
* Python programming principles
* Data validation
* File handling
* JSON data export
* Software testing and debugging
* Version control using Git and GitHub

## Author

Created by Alex Magson

GitHub: https://github.com/alex-mags

## License

This project is intended for educational purposes as part of a software development coursework project.
