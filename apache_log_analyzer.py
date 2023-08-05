#!/usr/bin/env python3

# Ricky Patel
# rpatel7@madisoncollege.edu
# Apache log analyzer project MILESTONE 1; create var and print it, take an input and store it.

import getopt, sys, subprocess, argparse, requests, bs4

#fuction calls website for info on most requested IP
def IPLookUp(IP):
    url = f"https://tools.keycdn.com/geo?host={IP}"
    response = requests.get(url)
    return response.text

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

    #create argumnet for input for file name
    parser = argparse.ArgumentParser(description = "Parser")

    #argument for file name
    parser.add_argument("-f", "--filenmae", dest = "filename", required = True, type = str, help = "Enter File Name")

    #getting arguments user entered
    args = parser.parse_args()

    #results = IPAddressCount(args.filename)
    results = IPAddressCount("m5-access.log")

    #get just the IP of the IP that is seen the most
    highest_ip = results.split("\n")[-2].split()[1]

    print(highest_ip)

    highest_url = IPLookUp(highest_ip)
    print(highest_url[:250])

    myHTML = bs4. BeautifulSoup(highest_url, features="html.parser")
    print(myHTML.find_all("dd",class_ = "col-8 text-monospace")[1].text)

    apache_log_analysis = open("apache_analysis.txt", "w")

    apache_log_analysis.write(highest_url)

    apache_log_analysis.close

    
            
if __name__ == "__main__":
    main()