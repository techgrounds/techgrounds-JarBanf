import os.path # import os.path
import csv # import csv module
from csv import writer # import writer class from csv module

# define emppty dictionary
userDict = {}

# ask user to input details
firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
jobTitle = input("Enter job title: ")
company = input("Enter company: ")

# store details in dictionary "userDict"
userDict["first name"] = firstName
userDict["last name"] = lastName
userDict["job title"] = jobTitle
userDict["company"] = company

# list of column names
fieldNames = userDict.keys()

# dictionary values that we want to add as a new row
dictValues = userDict.values()

# name of csv file
fileName = './09_Python/includes/user_details.csv'

# check if file already exists
check_file = os.path.isfile(fileName)

if check_file == True:
    #if file exists, append to file
    print("CSV file already exist, appending to file..")
    # APPENDING to csv file
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open (fileName, "a") as f_object:
        # Pass this file object to csv.writer() 
        # and get a writer object
        writer_object = writer(f_object)
        
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(dictValues)

        # Close the file object
        f_object.close()
else:
    # else file doesn't exist, write to file
    print("CSV file doesn't exist, creating file..")
    # WRITING to csv file
    with open(fileName, "w", newline="") as csvfile: 
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)

        # writing headers (fieldnames)
        writer.writeheader()

        # writing data rows
        writer.writerow(userDict)