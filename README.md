# Hospital Management System (OOP & File I/O)

A lightweight Python application demonstrating core Object-Oriented Programming (OOP) concepts, persistent file handling, and robust exception handling within a healthcare domain.

## Features

- **OOP Architecture**: Built on abstract base classes, strong data encapsulation, and class inheritance.
- **Dynamic Medical Records**: Creates timestamped consultation records with auto-incrementing tracking IDs.
- **File Persistence**: Exports treatment documentation and appends billing fees directly to external text files.
- **Input Validation & Safety**: Employs exception handling to protect file operations and validate numerical fee entries.

---

## Architecture & OOP Design
      +-----------------------+
      |  Person (Abstract)    |
      +-----------------------+
                 |
   +-------------+-------------+
   |                           |
+--------------+         +---------------+
|    Doctor    |         |    Patient    |
+--------------+         +---------------+
The project uses a clean class hierarchy to model real-world hospital interactions:

## File Handling & Exception Safety

### File Operations
The system exports prescription and billing records directly to `Treatment-and-Prescription.txt`:
1. **Write Mode (`"w"`)**: Generates a clean treatment sheet containing patient details, visit timestamp, and clinical notes.
2. **Append Mode (`"a"`)**: Appends the consultation fee to the existing document without overwriting previous data.

### Exception Handling
- **Data Validation (`try/except (ValueError, TypeError)`)**: Converts and verifies fee inputs to prevent negative or non-numeric values.
- **I/O Safeguards (`try/except Exception`)**: Wraps file operations to handle path errors, missing directories, or permission issues cleanly.


### treatment paper going to look like 
"""
<<  Treatment and Prescription  >>
Patient ID : 987654
Name       : Khaldoon
Time: 07:18PM in 2026-09-06
description: 
    Patient reported minor joint pain.
Fee: 50.0$
"""
