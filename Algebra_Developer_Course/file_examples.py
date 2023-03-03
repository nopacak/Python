# WRITE TO FILE
# Open file
file_stream = open("example.txt", "w", encoding="utf-8")

# Write in file
file_stream.write("Hello from Python.")

# Close file
file_stream.close()


# READ FROM FILE
# Open file
file_stream = open("example.txt", "r", encoding="utf-8")

# Read file
file_data = file_stream.read()

# Close file
file_stream.close()

print(f"Text in file is: {file_data}")
# Text in file is: Hello from Python.


# Try, except, finally block

# Open File
# Read / Write to file
# Close File

try:
    file_stream = open("example.txt", "w", encoding="utf-8")
    file_stream.write("Hello from try-except-finally block")
except Exception as e:
    print(f"Error! -> {e}")
finally:
    file_stream.close()



# PHONEBOOK

id = 1
while True:
    name = input("Please write contact name: ")
    surname = input("Please write contact surname: ")
    mobile = input("Please write contact mobile number: ")

    contact = f"{id}, {name}, {surname}, {mobile}\n"    #CSV format -> comma separated values
    id += 1

    try:
        file_stream = open("phonebook.txt", "w", encoding="utf-8")
        file_stream.write(contact)
    except Exception as e:
        print(f"Error! -> {e}")
    finally:
        file_stream.close()

    if input("Would you like to add another contact? (y/n)") != "y":
        break





# Context manager  ->  Automatically closes file stream
try:
    with open("example.txt", "w", encoding="utf-8") as file_stream:
        file_stream.write("Hello from context manager")
except Exception as e:
    print(f"Error! -> {e}")


class Contact:
    def __init__(self, id, name, surname, mobile) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.mobile = mobile

    def file_data(self):
        return f"{self.id}, {self.name}, {self.surname}, {self.mobile}\n"
    
id = 1
while True:
    name = input("Please write contact name: ")
    surname = input("Please write contact surname: ")
    mobile = input("Please write contact mobile number: ")

    contact = Contact(id=id, name=name, surname=surname, mobile=mobile)
    id += 1

    try:
        with open("phonebook.txt", "a", encoding="utf-8") as file_stream:
            file_stream.write(contact.file_data())
    except Exception as e:
        print(f"Error! -> {e}")

    if input("Would you like to add another contact? (y/n) ") != "y":
        break


try:
    with open("phonebook.txt", "r", encoding="utf-8") as file_stream:
        for line in file_stream:
            print(line.strip())
except Exception as e:
    print(f"Error! -> {e}")

    