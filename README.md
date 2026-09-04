# 📚 Library Management System

A simple, console-based **Library Management System** built in Python. It allows users to add, view, search, issue, return, update, and delete books, with all data stored persistently in a local JSON file.

**Developed by:** Satyam Tiwari

---

## 🧾 Project Overview

This project was built as a Computer Science project to demonstrate core programming concepts including file handling, JSON data storage, functions, control flow, and basic CRUD (Create, Read, Update, Delete) operations — all through a clean, menu-driven command-line interface.

---

## ✨ Features

- **Add Book** — Add new books with title, author, genre, and number of copies.
- **View All Books** — Display the full library catalog in a formatted table.
- **Search Book** — Search books by title, author, or genre.
- **Issue Book** — Issue an available book to a borrower and track the issue date.
- **Return Book** — Return a previously issued book and update available stock.
- **Update Book Details** — Edit a book's title, author, or genre.
- **Delete Book** — Remove a book from the library.
- **Persistent Storage** — All data is automatically saved to and loaded from `books.json`.
- **Error Handling** — Handles invalid input, missing files, and corrupted data gracefully.

---

## 🗂️ Project Structure

```
Library_Management_System/
│
├── main.py         # Main program with all logic and the CLI menu
├── books.json       # JSON file used to store book records
└── README.md        # Project documentation (this file)
```

---

## ⚙️ Requirements

- Python 3.6 or higher
- No external libraries required (uses only Python's built-in `json`, `os`, and `datetime` modules)

---

## ▶️ How to Run

1. Make sure Python 3 is installed on your system.
2. Open a terminal / command prompt.
3. Navigate to the project folder:
   ```bash
   cd Library_Management_System
   ```
4. Run the program:
   ```bash
   python main.py
   ```
5. Use the on-screen menu (options 1–8) to interact with the system.

---

## 📖 Menu Options

| Option | Action                |
|--------|------------------------|
| 1      | Add Book               |
| 2      | View All Books         |
| 3      | Search Book            |
| 4      | Issue Book             |
| 5      | Return Book            |
| 6      | Update Book Details    |
| 7      | Delete Book            |
| 8      | Exit                   |

---

## 🗃️ Data Storage Format

Each book is stored in `books.json` as an object with the following structure:

```json
{
    "id": 1,
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "genre": "Fiction",
    "total_copies": 5,
    "available_copies": 3,
    "issued_to": [
        {
            "borrower": "Rahul Sharma",
            "issue_date": "2026-09-04"
        }
    ]
}
```

If `books.json` is missing or empty, the program automatically creates a fresh, valid file on startup — so the project always runs without manual setup.

---

## 🚀 Possible Future Enhancements

- Add a graphical user interface (GUI) using Tkinter
- Add due dates and fine calculation for overdue books
- Export the catalog to CSV or PDF
- Add user authentication (Admin/Student login)
- Migrate storage from JSON to a proper database (SQLite)

---

## 👤 Author

**Satyam Tiwari**
Computer Science Project — Library Management System

---

## 📄 License

This project was created for Academic/Educational purposes.