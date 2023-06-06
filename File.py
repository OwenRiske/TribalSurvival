

#function to make it easier to open the file
def file(File_name):
    file = open(File_name, "a+")
    return file

#turn the info file into a list
def read_file(file):
    f = open(f"{file}.txt", "r")
    return f.read().split("\n")


#clear all information that is stored
def clear(clearFile):
    clearFile.truncate(0)
