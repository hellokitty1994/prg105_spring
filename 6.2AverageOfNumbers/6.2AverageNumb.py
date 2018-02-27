# Write a program that uses the numbers.txt file, which contains a series of integers.
# Your program will calculate the average of all of
# the numbers stored in the file and display the total on the screen.
# Format to show a maximum of two numbers to the right of the decimal point.
def main():
    try:
        input_file = open('numbers.txt' , 'r')
    except exception as errorMSG:
        print("unknown file")
    else:
        total = 0
        number_of_lines = 0
        line = input_file.readline()
    while line != "":
        number_of_lines += 1
        total += int(line)
        record = input.file.redline()
        record = record.rstrip('\n')
        avarage = total / input_file
print("The avarage is")
main ()
