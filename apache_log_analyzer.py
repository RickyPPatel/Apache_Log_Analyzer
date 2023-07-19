#!/usr/bin/env python3

# Ricky Patel
# rpatel7@madisoncollege.edu
# Apache log analyzer project MILESTONE 1; create var and print it, take an input and store it.
def ParseLogEntry(apache_log_entry):
#split entries from log file 
    #remove all double quotes from string
    log_file = entries.replace('"', '')

    #split and print HTTP status code and IP address
    log_split = log_file.split(" ")
    return(log_split)

def main():
    #take command line argument input
    import getopt, sys
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        print("Apache log analyzer; would you like to continue?/n")
        user_input = input("y, yes, or yeah for yes, any other input with be a no\n")

    #input taken and evaluted
    vaild_input = ["y", "yes", "yeah"]
    if not user_input.lower() in vaild_input:
        print("you choose not to continue")
        exit(0)

    #read apache log entries
    with open("m5-access.log", "r") as log_file:
        log_entries = log_file.readlines()

    #create file and assign var to it
    hFile = open("apache_analysis.txt", "w")

    #create an empty dictionary to store summary information about our apache log file 
    apache_log_summary = {}

    log_split = ParseLogEntry(log_entries)

    #checks for HTTPS code over 400 and prints them
    if int(log_split[8]) >= 400:
        #print IP and HTTPS status code
        print(f"", log_split[0], "-", log_split[8])

        #assign IP and HTTPS status code to log_line
        #log_line = (f"", log_split[0], "-", log_split[8])

    if log_split[0] in apache_log_summary:
        apache_log_summary[log_split[0]] += 1
    else:
        apache_log_summary[log_split[0]] = 1

    for ip in apache_log_summary:
        if apache_log_summary[ip] >= 5:
            summary = f"{log_split[0]} has {apache_log_summary[ip]}"
            hFile.write(summary + "\n")
            
if __name__ == "__main__":
    main()