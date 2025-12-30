import sys
from library.db import init_db
from library import services

def usage():
    print("""
Commands:
  add-author "Name"
  add-book "Title" author_id
  list
  borrow book_id
  report
""")

def main():
    init_db()

    if len(sys.argv) < 2:
        usage()
        return

    cmd = sys.argv[1]

    if cmd == "add-author":
        services.add_author(sys.argv[2])
        print("Author added")

    elif cmd == "add-book":
        services.add_book(sys.argv[2], int(sys.argv[3]))
        print("Book added")

    elif cmd == "list":
        for b in services.list_books():
            print(b)

    elif cmd == "borrow":
        services.borrow(int(sys.argv[2]))
        print("Book borrowed")

    elif cmd == "report":
        services.export_csv()

    else:
        usage()

if __name__ == "__main__":
    main()
