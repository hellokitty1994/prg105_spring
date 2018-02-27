# Download the file
# Save it into the same project folder in pycharm that you are using for this project.
# your python file will
# 1.Read and Display the list of names from the file
# 2.Display the number of names that are read from the file
# (You will need a variable to keep a count of the number of items read from the file.)
def main():
   name_file = open('name.txt, 'r'')
   line = name_file.readline()
while record != "":
    print(line.rstrip("\n"))
    line = name_file.readline()
main()
