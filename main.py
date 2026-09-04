"""
==============================================================
 Library Management System
==============================================================
 Project      : Library Management System (Console Based)
 Developed By : Satyam Tiwari
 Language     : Python 3
 Description  : A simple, file-based Library Management System
                that allows adding, viewing, searching, issuing,
                returning, updating and deleting books. All data
                is stored persistently in 'books.json'.
==============================================================
"""

import json
import os
from datetime import datetime

DATA_FILE = "books.json"


# ---------------------------------------------------------------
# Data Handling Functions
# ---------------------------------------------------------------

def load_books():
    """Load the book records from the JSON file. Creates the file if missing."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
        return []

    try:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        print("Warning: books.json was corrupted. Starting with an empty library.")
        return []


def save_books(books):
    """Save the current list of book records back to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=4)


def get_next_id(books):
    """Generate the next available Book ID."""
    if not books:
        return 1
    return max(book["id"] for book in books) + 1


# ---------------------------------------------------------------
# Core Library Operations
# ---------------------------------------------------------------

def add_book(books):
    print("\n--- Add New Book ---")
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    genre = input("Enter genre: ").strip()

    while True:
        qty_input = input("Enter number of copies: ").strip()
        if qty_input.isdigit() and int(qty_input) > 0:
            quantity = int(qty_input)
            break
        print("Please enter a valid positive number.")

    if not title or not author:
        print("Title and Author cannot be empty. Book not added.")
        return

    new_book = {
        "id": get_next_id(books),
        "title": title,
        "author": author,
        "genre": genre if genre else "N/A",
        "total_copies": quantity,
        "available_copies": quantity,
        "issued_to": []
    }

    books.append(new_book)
    save_books(books)
    print(f"'{title}' added successfully with Book ID {new_book['id']}.")


def view_books(books):
    print("\n--- Library Catalog ---")
    if not books:
        print("No books found in the library.")
        return

    header = f"{'ID':<5}{'Title':<30}{'Author':<20}{'Genre':<15}{'Available':<10}{'Total':<6}"
    print(header)
    print("-" * len(header))
    for book in books:
        print(f"{book['id']:<5}{book['title'][:28]:<30}{book['author'][:18]:<20}"
              f"{book['genre'][:13]:<15}{book['available_copies']:<10}{book['total_copies']:<6}")


def search_book(books):
    print("\n--- Search Book ---")
    keyword = input("Enter title, author, or genre to search: ").strip().lower()

    results = [
        b for b in books
        if keyword in b["title"].lower()
        or keyword in b["author"].lower()
        or keyword in b["genre"].lower()
    ]

    if not results:
        print("No matching books found.")
        return

    print(f"\nFound {len(results)} result(s):")
    for book in results:
        print(f"\nID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Genre: {book['genre']}")
        print(f"Available Copies: {book['available_copies']} / {book['total_copies']}")


def find_book_by_id(books, book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None


def issue_book(books):
    print("\n--- Issue Book ---")
    try:
        book_id = int(input("Enter Book ID to issue: ").strip())
    except ValueError:
        print("Invalid Book ID.")
        return

    book = find_book_by_id(books, book_id)
    if not book:
        print("Book not found.")
        return

    if book["available_copies"] <= 0:
        print(f"Sorry, '{book['title']}' is currently out of stock.")
        return

    borrower = input("Enter borrower's name: ").strip()
    if not borrower:
        print("Borrower name cannot be empty.")
        return

    book["available_copies"] -= 1
    book["issued_to"].append({
        "borrower": borrower,
        "issue_date": datetime.now().strftime("%Y-%m-%d")
    })

    save_books(books)
    print(f"'{book['title']}' issued to {borrower} successfully.")


def return_book(books):
    print("\n--- Return Book ---")
    try:
        book_id = int(input("Enter Book ID to return: ").strip())
    except ValueError:
        print("Invalid Book ID.")
        return

    book = find_book_by_id(books, book_id)
    if not book:
        print("Book not found.")
        return

    if not book["issued_to"]:
        print("No copies of this book are currently issued.")
        return

    print("Currently issued to:")
    for i, record in enumerate(book["issued_to"], start=1):
        print(f"{i}. {record['borrower']} (Issued on {record['issue_date']})")

    try:
        choice = int(input("Enter the number of the borrower returning the book: ").strip())
        if choice < 1 or choice > len(book["issued_to"]):
            raise ValueError
    except ValueError:
        print("Invalid selection.")
        return

    returned_record = book["issued_to"].pop(choice - 1)
    book["available_copies"] += 1
    save_books(books)
    print(f"Book returned by {returned_record['borrower']} successfully.")


def update_book(books):
    print("\n--- Update Book Details ---")
    try:
        book_id = int(input("Enter Book ID to update: ").strip())
    except ValueError:
        print("Invalid Book ID.")
        return

    book = find_book_by_id(books, book_id)
    if not book:
        print("Book not found.")
        return

    print("Leave field blank to keep the current value.")
    new_title = input(f"Title [{book['title']}]: ").strip()
    new_author = input(f"Author [{book['author']}]: ").strip()
    new_genre = input(f"Genre [{book['genre']}]: ").strip()

    if new_title:
        book["title"] = new_title
    if new_author:
        book["author"] = new_author
    if new_genre:
        book["genre"] = new_genre

    save_books(books)
    print("Book details updated successfully.")


def delete_book(books):
    print("\n--- Delete Book ---")
    try:
        book_id = int(input("Enter Book ID to delete: ").strip())
    except ValueError:
        print("Invalid Book ID.")
        return

    book = find_book_by_id(books, book_id)
    if not book:
        print("Book not found.")
        return

    confirm = input(f"Are you sure you want to delete '{book['title']}'? (y/n): ").strip().lower()
    if confirm == "y":
        books.remove(book)
        save_books(books)
        print("Book deleted successfully.")
    else:
        print("Deletion cancelled.")


# ---------------------------------------------------------------
# Menu / Program Driver
# ---------------------------------------------------------------

def print_banner():
    print("=" * 55)
    print("        LIBRARY MANAGEMENT SYSTEM".center(55))
    print("        Developed by Satyam Tiwari".center(55))
    print("=" * 55)


def print_menu():
    print("\n1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Update Book Details")
    print("7. Delete Book")
    print("8. Exit")


def main():
    books = load_books()
    print_banner()

    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            issue_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            update_book(books)
        elif choice == "7":
            delete_book(books)
        elif choice == "8":
            print("\nThank you for using the Library Management System.")
            print("Project by Satyam Tiwari. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 8.")


if __name__ == "__main__":
    main()