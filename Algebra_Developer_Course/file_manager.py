import os

def file_path_exsists(file_path:str) -> bool:
    """Method that returns True or False, depending whether "file_path" exists or no.
    File connection will be open for reading.
    """
    return os.path.exists(file_path)



def open_file_path_for_reading(file_path: str) -> str:
    if not file_path_exsists(file_path):
        return f"File {file_path} does not exist!"
    try:
        file_stream = open(file_path, "r", encoding="utf-8")
        return file_stream
    except Exception as e:
        return f"Error! -> {e}"



def write_to_file(text: str, file_path: str) -> None:
    """Method for writing to file at "file_path"
    Uses "w" option for writing
    Writing content is saved in "text" variable
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file_stream:
            file_stream.write(text)
    except Exception as e:
        return f"Error! -> {e}"
    

def append_to_file(text: str, file_path: str) -> None:
    """Method for appending to file at "file_path"
    Uses "a" option for appending
    Appended content is saved in "text" variable
    """
    try:
        with open(file_path, "a", encoding="utf-8") as file_stream:
            file_stream.write(text)
    except Exception as e:
        return f"Error! -> {e}"
    

def read_from_file(file_path: str) -> None:
    """Method for reading from file at "file_path"
    Uses "r" option for reading
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file_stream:
            return file_stream.read()
    except Exception as e:
        return f"Error! -> {e}"