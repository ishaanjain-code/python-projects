def add_contact(contact_book):
    name=input("enter name of the contact: ").strip()
    if name in contact_book:
        response=input("contact already exist with the same name\ndoyou want to over write it (yes/no): ").strip()
        if response.lower()!="yes":
            print("contact not added")
            return contact_book
    number=(input("enter number of the contact: "))
    if number in contact_book.values():
        response=input("contact already exist with the same number\ndoyou want to over write it (yes/no): ").strip()
        if response.lower()!="yes":
            print("contact not added")
            return contact_book
    if number.isdigit() and len(number)==10:
        contact_book[name]=number
    else :
        print("invaild number ⚠")
    return contact_book


def delete_contact(contact_book):
    del_con=input("enter the name or the number you want to delete from your contacts: ")
    key_del=None
    if del_con.isdigit():
        if del_con in contact_book.values():
            for name,number in contact_book.items():
                if number== del_con:
                    key_del=name
                    break
            if key_del:
                del contact_book[key_del]
                print("contact deleted")
                return contact_book
        elif del_con in contact_book:
            del contact_book[del_con]
            print("contact deleted")
            return contact_book
        else :
            return "contact does not exist"
    else :
        if del_con in contact_book:
            del contact_book[del_con]
            print("contact deleted")
            return contact_book
        else:
            return "contact does not exist "
        

def search_contact(contact_book):
    name = input("Enter name to search: ").strip()
    if name in contact_book:
        print(f" {name}: {contact_book[name]}")
    else:
        print(" Contact not found.")
        
def contact_book_app():
    phone_book = {}

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(phone_book)
        elif choice == "2":
            delete_contact(phone_book)
        elif choice == "3":
            search_contact(phone_book)
        elif choice == "4":
            print("Exiting Contact Book.")
            break
        else:
            print(" Invalid choice. Try again.")


contact_book_app()

           

    