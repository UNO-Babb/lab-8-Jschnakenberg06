#ProcessData.py
#Name:Jonas Schnakenberg 
#Date:
#Assignment:

import random

def main():
    # Open the files we will be using
    inFile = open("names.dat", 'r')
    outFile = open("StudentList.csv", 'w')

    # Write the header for the CSV file
    outFile.write("Last Name, First Name, User ID, Major-Year\n")

    # Process each line of the input file and output to the CSV file
    for line in inFile:
        data = line.split()

        first = data[0]
        last = data[1]
        idNum = data[3]
        year = data[5]
        major = data[6]

        student_id = makeID(first, last, idNum)
        major_year = makeMajorYear(major, year)

        output = f"{last},{first},{student_id},{major_year}\n"
        outFile.write(output)

    # Close files in the end to save and ensure they are not damaged
    inFile.close()
    outFile.close()

def makeID(first, last, idNum):
    # Ensure last name is at least 5 characters
    while len(last) < 5:
        last += "x"

    id = first[0] + last + idNum[-3:]
    return id

def makeMajorYear(major, year):
    maj = major[:3]

    if year == "Freshman":
        yr = "FR"
    elif year == "Sophomore":
        yr = "SP"
    elif year == "Junior":
        yr = "JR"
    elif year == "Senior":
        yr = "SR"
  
    return f"{maj}-{yr}"

if __name__ == '__main__':
    main()