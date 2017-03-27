f = open('report.csv')
f1 = open('output.csv', 'a')

string = "";
first = True;

for line in f.readlines():

    if 'License' in line:
        string += "\n"
        f1.write(string)
        first =True
    	string = ""
    
    elif (first or not 'Photo' in line and 'First Name' in line or 'Last Name' in line or 'IP Whitelisted' in line or 'Account Suspended' in line or 'Creation Time' in line or 'Last login' in line or 'Licenses' in line):
		string += ","
		string += line[0:-1]
		first = False
		

f1.close()
f.close()
