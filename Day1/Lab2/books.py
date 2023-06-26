books = {
    "J.K. Rowling": ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban"],
    "George R.R. Martin": ["A Game of Thrones", "A Clash of Kings", "A Storm of Swords"],
    "Jane Austen": ["Pride and Prejudice", "Sense and Sensibility", "Emma"]
}

author_name = input("Enter the author name: ").lower()

# Remove punctuation from user input
author_name = author_name.replace(".", "")

found_author = None
for author in books:
    # Remove punctuation from author names
    author_cleaned = author.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "")

    if author_cleaned == author_name:
        found_author = author
        break

if found_author:
    books_by_author = ", ".join(books[found_author])
    print(f"The books by {found_author} are: {books_by_author}")
else:
    print(f"No books found for {author_name}.")


