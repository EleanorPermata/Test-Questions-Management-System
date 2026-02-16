# Test Question Management System (TQMS)

Programming with Python (102023-MAL)
Asia Pacific University  

## 📌 Overview

The Test Question Management System (TQMS) is a terminal-based academic management application developed using Python. The system enables structured management of user accounts, subjects, question banks, and exam paper generation through role-based access control.

This project demonstrates practical implementation of Python fundamentals including file handling, modular programming, input validation, and logical system design.


## 🎯 Key Features

### 🔐 Role-Based Authentication
- Login system with maximum 3 attempts  
- Separate access control for:
  - Admin  
  - Lecturer  
  - Exam Personnel  
- Persistent credential storage using text files  


### Admin Module
- Create, edit, and delete user accounts  
- Add and manage subjects  
- Add and manage topics  


### Lecturer Module
- Create and manage question bank  
- Support for Multiple Choice and Subjective questions  
- Organize questions by subject and topic  
- Edit and review stored questions  


### Exam Personnel Module
- Generate two structured exam sets (Set 1 and Set 2)  
- Section A: Minimum 5 MCQs  
- Section B: Minimum 3 Subjective questions  
- Modify and review exam papers  


## 🗂️ System Architecture

The application follows a modular, function-based structure with persistent data storage using plain text files.

Data files used:
- `users.txt`
- `subjects.txt`
- `topics.txt`
- `questions.txt`
- `exam_sets.txt`

Credentials are stored in plaintext for academic demonstration purposes.


## ⚙️ Technologies Used

- Python 3  
- File handling (read/write operations)  
- Conditional statements and loops  
- Functions and modular programming  
- Input validation  
- Exception handling  
- Command Line Interface (CLI)  


## ▶️ How to Run

1. Download all repository files.  
2. Ensure all `.py` and `.txt` files are placed in the same directory.  
3. Open the folder in any Python IDE (e.g., VSCode or PyCharm).  
4. Run:

```bash
python Test_Question_Management_System_Final.py
```

5. Login using credentials stored in `users.txt`.


## ⚠️ Limitations

- Command-line interface only (no GUI)  
- No password encryption  
- No database integration  
- Single-user execution model  


## 🚀 Future Improvements

- Implement password hashing  
- Integrate relational database (MySQL / SQLite)  
- Develop graphical user interface  
- Add search and filtering capabilities  
- Implement reporting features  


## 👥 Contributors

- Eleanor Permata Fry (TP072606)
- Eshaal Irshad (TP077658) 
- Honoka Oi (TP074913)
- Shuhd Fadhl Hussein Ghaleb (TP076842)

