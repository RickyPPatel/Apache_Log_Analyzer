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

#assign apache log entries
log_file = '111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"\n111.222.333.124 HOME - [01/Feb/1998:01:08:46 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 28083 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"\n111.222.333.125 AWAY - [01/Feb/1998:01:08:53 -0800] "GET /bannerad/ad7.gif HTTP/1.0" 401 9332 "http://www.referrer.com/bannerad/ba_ad.htm" "Mozilla/4.01 (Macintosh; I; PPC)"\n111.222.333.126 AWAY - [01/Feb/1998:01:09:14 -0800] "GET /bannerad/click.htm HTTP/1.0" 501 207 "http://www.referrer.com/bannerad/menu.htm" "Mozilla/4.01 (Macintosh; I; PPC)"'

#remove all double quotes from string
log_file = log_file.replace('"', '')

#split entries from log file 
log_entries = log_file.split("\n")
for entries in log_entries:
    #print(x)
    #assign apache log entry

    #remove all double quotes from string
    log_file = entries.replace('"', '')

    #Getting ip
    IP = log_file[:15]

    #print and format
    print(f"Log form request:", IP.center(22,'*'))

    #split and print 9th element
    log_split = log_file.split(" ")
    print(f"Return Code:", log_split[8])