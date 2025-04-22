This repository contains the source code and data files for a **Python-based Test Questions Management System (TQMS)** developed as part of a group assignment for the **Programming with Python** module.

## ❗Overview

The TQMS is a terminal-based system that allows academic admins, lecturers, and exam unit personnel to manage user accounts, questions, and exam papers efficiently. The system emphasizes modular programming, file-based data storage, and user-specific role functionality.

## Key Features
**Login System**
  - 3 login attempts limit for all user roles.

**Admin Features**
  - Add, edit, and delete user accounts (lecturers and exam personnel).
  - Add and manage subjects and topics.

**Lecturer Features**
  - Add, edit, and view test questions by subject and topic.

**Exam Personnel Features**
  - Create two sets of exam papers (Set 1 & Set 2):
    - **Section A:** Multiple Choice Questions (minimum 5)
    - **Section B:** Subjective Questions (minimum 3)
  - Modify and view exam sets.

## Data Storage & Structure

- All data is stored in plain `.txt` files for simplicity.
- Login credentials are stored in `users.txt` (plaintext, no encryption).
- Questions, subjects, and exam sets are stored in separate text files.
- Terminal-based interface with no GUI (focus on programming logic).

## ❓How to Run
1. Download all the files in repository.
2. Ensure all files are within the same folder.
3. Run the `Test Question Management System_Final.py` file.
