#Ricky Patel
#rpatel7@madisoncollege.edu
#Apache log analyzer project MILESTONE 1; create var and print it, take an input and store it.

#added output and printed
output = "Apache log analyzer project; continue?"
print(output,"\n")

#input taken and printed
input = input("y for yes n or no\n")
print("we have recived the following input: ", input)

# if user does not want to continue
if input == "n":
    exit(0)

#MILESTONE 2

#assign apache log entry
log_file = '111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"'

#remove all double quotes from string
log_file = log_file.replace('"', '')

#Getting ip
IP = log_file[:15]

#print and format
print(f"Log form request:", IP.center(22,'*'))

#split and print 9th element
log_split = log_file.split(" ")
print(f"Return Code:", log_split[8])