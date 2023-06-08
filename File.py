#Owen Riske

#function to make it easier to open the file
def file(File_name):
    file = open(File_name, "r+")
    return file

#turn the info file into a list
def read_file(file):
    f = open(f"{file}.txt", "r+")
    return f.read().split("\n")

def write_file(StringToBeWritten, file_name):
    file1 = open(f"{file_name}.txt", "w")
    file1.writelines(StringToBeWritten)
    file1.close()

#clear all information that is stored
def clear(clearFile):
    clearFile.truncate(0)
