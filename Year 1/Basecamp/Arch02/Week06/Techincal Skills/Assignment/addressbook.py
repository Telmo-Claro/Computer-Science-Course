import os
import sys
import json


def read_from_json(filename) -> list:
    address_book = list()
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        json_data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in json_data:
            address_book.append(contact)
    return address_book

def write_to_json(filename, address_book: list) -> None:
    json_object = json.dumps(address_book, indent=4)
    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


def display(address_book: list):
    for contact in address_book:
        client_id = contact["id"]
        first_name = contact["first_name"]
        last_name = contact["last_name"]
        emails = ", ".join(contact["emails"])
        phone_numbers = ", ".join(contact["phone_numbers"])
        print("======================================")
        print(f"Position: {client_id}")
        print(f"First name: {first_name} ")
        print(f"Last name: {last_name}")
        print(f"Emails: {emails}")
        print(f"Phone numbers: {phone_numbers}")
        print("======================================")
    return address_book


def list_contacts(address_book):
    address_book = sorted(address_book, key=lambda d: d["first_name"])
    return address_book


def add_contact(address_book):
    # todo: implement this function
    contact_id = int(len(address_book)) + 1
    first_name_input = input("First name: ")
    last_name_input = input("Last name: ")
    emails_input = input("Emails: ").split(",")
    phone_numbers_input = input("Phone number(s): ")
    new_contact = {
        "id": contact_id,
        "first_name": first_name_input,
        "last_name": last_name_input,
        "emails": emails_input,
        "phone_numbers": [phone_numbers_input],
    }
    address_book.append(new_contact)
    write_to_json("contacts.json", address_book)
    return address_book


def remove_contact(address_book):
    # todo: implement this function
    id_to_remove = int(input("Id to remove: "))
    for contacts in address_book[:]:
        if "id" in contacts and contacts["id"] == id_to_remove:
            address_book.remove(contacts)


"""
merge duplicates (automated > same fullname [firstname & lastname])
"""


def merge_contacts(address_book):
    address_book = read_from_json("contacts.json")
    # todo: implement this function
    list_of_contacts = []
    temporary_match_checker = []
    for item in address_book:
        ...
    return

print(merge_contacts("contacts.json"))



def read_from_json(filename) -> list:
    address_book = list()
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        json_data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in json_data:
            address_book.append(contact)
    return address_book


def main(json_file):
    address_book = read_from_json(json_file)
    while True:
        print(
            """[L] List contacts
[A] Add contact
[R] Remove contact
[M] Merge contacts
[Q] Quit program"""
        )
        choice = input("Input: ").lower()
        if choice == "l":
            display(address_book)
        elif choice == "a":
            add_contact(address_book)
        elif choice == "r":
            remove_contact(address_book)
        elif choice == "m":
            merge_contacts(address_book)
        elif choice == "q":
            break
        else:
            print("Input error, try again: ")


if __name__ == "__main__":
    main("contacts.json")
