import json

# File to save library data
LIBRARY_FILE = "library.json"

# Load library from file
def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def main():
    library = load_library()

    while True:
        print("\n📚 Personal Library Manager")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            year = input("Enter the publication year: ")
            genre = input("Enter the genre: ")
            read_status = input("Have you read this book? (yes/no): ").lower() == 'yes'
            
            library.append({
                "Title": title,
                "Author": author,
                "Year": year,
                "Genre": genre,
                "Read": read_status
            })
            save_library(library)
            print("Book added successfully!")

        elif choice == "2":
            title_to_remove = input("Enter the title of the book to remove: ")
            library = [book for book in library if book["Title"].lower() != title_to_remove.lower()]
            save_library(library)
            print(f"'{title_to_remove}' removed successfully!")

        elif choice == "3":
            search_query = input("Enter the title or author to search for: ")
            results = [
                book for book in library
                if search_query.lower() in book['Title'].lower() or search_query.lower() in book['Author'].lower()
            ]

            if results:
                for idx, book in enumerate(results, start=1):
                    print(f"{idx}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {'Read' if book['Read'] else 'Unread'}")
            else:
                print("No matching books found!")

        elif choice == "4":
            if library:
                for idx, book in enumerate(library, start=1):
                    print(f"{idx}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {'Read' if book['Read'] else 'Unread'}")
            else:
                print("Your library is empty!")

        elif choice == "5":
            total_books = len(library)
            read_books = sum(1 for book in library if book['Read'])
            percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

            print(f"Total books: {total_books}")
            print(f"Books read: {read_books}")
            print(f"Percentage read: {percentage_read:.2f}%")

        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":

