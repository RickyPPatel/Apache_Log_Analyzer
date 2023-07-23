#!/usr/bin/env python3

# Ricky Patel
# rpatel7@madisoncollege.edu
# Apache log analyzer project MILESTONE 1; create var and print it, take an input and store it.

import getopt, sys, subprocess

#processes an Apache log file using shell commands, counts the occurrences of each IP address, and returns 5 IP addresses with the highest occurrence counts.
def IPAddressCount(apache_log_file_name):
    command = f"cat {apache_log_file_name} | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5"
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    return result.stdout.decode()

#splits the entries in the files
def ParseLogEntry(apache_log_entry):
    #remove all double quotes from string
    log_file = apache_log_entry.replace('"', '')

    #split the file
    log_split = log_file.split(" ")
    return(log_split[0], log_split[8])

#main function
def main():
    
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        print("Apache log analyzer; would you like to continue?\n")
        user_input = input("y, yes, or yeah for yes, any other input with be a no\n")

    #input taken and evaluted
    vaild_input = ["y", "yes", "yeah"]
    if not user_input.lower() in vaild_input:
        print("you choose not to continue")
        exit(0)

    results = IPAddressCount("m5-access.log")

    apache_log_analysis = open("apache_analysis.txt", "w")

    apache_log_analysis.write(results)
    print(results)

    apache_log_analysis.close
            
if __name__ == "__main__":
    main()