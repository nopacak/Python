from file_manager import file_path_exsists, write_to_file, read_from_file, append_to_file

file_exists = file_path_exsists("phonebook.txt")
print(file_exists)

content = "We're testing whether \n our \t file manager works."
file_path = "file_manager_test.txt"
write_to_file(content, file_path)

content = "\n\nWe're adding \n new line of text \t to our file because our file manager works!!"
append_to_file(content, file_path)

content = read_from_file(file_path)
print(content)
