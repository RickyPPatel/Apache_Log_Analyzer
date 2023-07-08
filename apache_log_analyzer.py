#!/usr/bin/env python3

# Ricky Patel
# rpatel7@madisoncollege.edu
# Apache log analyzer project MILESTONE 1; create var and print it, take an input and store it.

#added output and printed
output = "Apache log analyzer project; continue?"
print(output,"\n")

#input taken and printed
input = input("y for yes n or no\n")
print("we have recived the following input: ", input)

# if user does not want to continue
if input == "n":
    exit(0)

#Apache log analyzer project MILESTONE 2 and 3

#read apache log entries
with open("m4-access.log", "r") as log_file:
    log_entries = log_file.readlines()

hFile = open("apache_analysis.txt", "w")

#split entries from log file 
for entries in log_entries:
    #print(x)
    #assign apache log entry

    #remove all double quotes from string
    log_file = entries.replace('"', '')

    #split and print HTTP status code and IP address
    log_split = log_file.split(" ")

    #print IP and HTTPS status code
    print(f"", log_split[0], "-", log_split[8])

    #assign IP and HTTPS status code to log_line
    log_line = (f"", log_split[0], "-", log_split[8])
    
    #convert tuple to str
    log_line = ''.join(log_line)

    #write into file and add new line
    hFile.write(log_line)
    hFile.write("\n")


