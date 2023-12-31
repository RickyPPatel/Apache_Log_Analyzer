#!/usr/bin/env python3

# Ricky Patel
# rpatel7@madisoncollege.edu
# Apache log analyzer project MILESTONE 1; create var and print it, take an input and store it.

import getopt, sys, subprocess, argparse, requests, bs4, json

#fuction calls website for info on most requested IP
def IPLookUp(IP):
    headerVariable = {"x-apikey" : "a6547215279c8267d7ac7f0caaaa7f2e8bb6be401d9cdf43a427f8d6ce4e21fb"}
    url = f"https://virustotal.com/api/v3/ip_addresses/{IP}"
    print(url)
    response = requests.get(url, headers = headerVariable)
    return response.text

#processes an Apache log file using shell commands, counts the occurrences of each IP address, and returns 5 IP addresses with the highest occurrence counts.
def IPAddressCount(apache_log_file_name):
    command = f"cat {apache_log_file_name} | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5"
    result = subprocess.run(command, stdout = subprocess.PIPE, shell=True)
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
    highest_IP = results.split("\n")[-2].split()[1]

    print(highest_IP)

    #getting json info from api
    IP_info = IPLookUp(highest_IP)

    #turning the json file to a dict
    IP_info = (json.loads(IP_info))

    category = (json.dumps(IP_info["data"]["attributes"]["last_analysis_results"]["BitDefender"]["category"], indent=4).replace('"', ''))

    #print the Bitdefender category
    print(f"Bitdefender category is:", category)

    #put number of requests for each log entrie in a file
    apache_log_analysis = open("apache_analysis.txt", "w")
    apache_log_analysis.write(results)
    apache_log_analysis.close
            
if __name__ == "__main__":
    main()