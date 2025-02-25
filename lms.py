import os
import json

# ANSI escape codes for colored text
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"

# Library List
library = []

# Load books from file (if exists)
def load_from_file():
    global library
    if os.path.exists("library.txt"):
        with open("library.txt", "r") as file:
            library = json.load(file)
        print(f"{GREEN}Library data loaded successfully!{RESET}\n")
    else:
        print(f"{YELLOW}No saved library found. Starting fresh.{RESET}\n")

# Save books to file
def save_to_file():
    with open("library.txt", "w") as file:
        json.dump(library, file, indent=4)
    print(f"{GREEN}Library data saved successfully!{RESET}\n")

# Add a book
def add_book():
    print(f"{CYAN}\n--- Add a New Book ---{RESET}")
    title = input("📖 Enter book title: ")
    author = input("✍️  Enter author name: ")
    
    try:
        year = int(input("📅 Enter year of publication: "))
    except ValueError:
        print(f"{RED}Invalid input! Year must be a number.{RESET}\n")
        return
    
    book = {"title": title, "author": author, "year": year, "status": "available"}
    library.append(book)
    print(f"{GREEN}✅ Book '{title}' added successfully!{RESET}\n")

# Display all books
def display_books():
    print(f"{CYAN}\n--- Library Books ---{RESET}")
    
    if not library:
        print(f"{YELLOW}No books in the library.{RESET}\n")
        return
    
    print(BOLD + "-" * 60 + RESET)
    print(f"{BOLD}{'Title':<25} {'Author':<20} {'Year':<6} {'Status':<10}{RESET}")
    print(BOLD + "-" * 60 + RESET)

    for book in library:
        status_color = GREEN if book["status"] == "available" else RED
        print(f"{book['title']:<25} {book['author']:<20} {book['year']:<6} {status_color}{book['status']:<10}{RESET}")
    
    print(BOLD + "-" * 60 + RESET + "\n")

# Update book status
def update_book():
    print(f"{CYAN}\n--- Update Book Status ---{RESET}")
    title = input("🔄 Enter the title of the book to update: ")
    
    for book in library:
        if book["title"].lower() == title.lower():
            new_status = input("📝 Enter new status (available/checked out): ").lower()
            if new_status in ["available", "checked out"]:
                book["status"] = new_status
                print(f"{GREEN}✅ Book '{title}' status updated successfully!{RESET}\n")
            else:
                print(f"{RED}Invalid status! Must be 'available' or 'checked out'.{RESET}\n")
            return
    
    print(f"{RED}Book not found.{RESET}\n")

# Delete a book
def delete_book():
    print(f"{CYAN}\n--- Delete a Book ---{RESET}")
    title = input("🗑️  Enter the title of the book to delete: ")
    
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print(f"{GREEN}✅ Book '{title}' deleted successfully!{RESET}\n")
            return
    
    print(f"{RED}Book not found.{RESET}\n")

# Search for a book
def search_book():
    print(f"{CYAN}\n--- Search for a Book ---{RESET}")
    title = input("🔍 Enter book title to search: ")
    
    for book in library:
        if book["title"].lower() == title.lower():
            print(f"{MAGENTA}📖 Found!{RESET}")
            print(BOLD + "-" * 50 + RESET)
            print(f"{BOLD}Title:{RESET} {book['title']}")
            print(f"{BOLD}Author:{RESET} {book['author']}")
            print(f"{BOLD}Year:{RESET} {book['year']}")
            print(f"{BOLD}Status:{RESET} {GREEN if book['status'] == 'available' else RED}{book['status']}{RESET}")
            print(BOLD + "-" * 50 + RESET + "\n")
            return
    
    print(f"{RED}Book not found.{RESET}\n")

# Main Menu
def main_menu():
    load_from_file()
    
    while True:
        print(f"\n{BOLD}{MAGENTA}📚 Library Management System 📚{RESET}")
        print(BOLD + "-" * 40 + RESET)
        print("1️⃣  Add Book")
        print("2️⃣  Display All Books")
        print("3️⃣  Update Book Status")
        print("4️⃣  Delete Book")
        print("5️⃣  Search for a Book")
        print("6️⃣  Save Library to File")
        print("7️⃣  Load Library from File")
        print("8️⃣  Exit")
        print(BOLD + "-" * 40 + RESET)
        
        choice = input("👉 Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            search_book()
        elif choice == "6":
            save_to_file()
        elif choice == "7":
            load_from_file()
        elif choice == "8":
            print(f"{YELLOW}🚪 Exiting... Goodbye!{RESET}")
            break
        else:
            print(f"{RED}❌ Invalid choice! Please enter a number between 1-8.{RESET}\n")

# Run the program
if __name__ == "__main__":
    main_menu()
