import sys
import os
import shutil
import subprocess

def Listing_1():
	listingsrc = '../web_server/listing_exec_app/lib/default_code/ch_13/Listing_13_1.py'
	shutil.copy(listingsrc, '../web_server/listing_exec_app/lib/default_code/ch_13/Listing_13_1Temp.py')
	f1 = open('../web_server/listing_exec_app/lib/default_code/ch_13/Listing_13_1Temp.py', 'a')
	f2 = open('Code_Listings/Appends/ap131.txt', 'r')
	for line in f2:
		f1.write(line)
	f1.close()
	f2.close()

	subprocess.call("python ../web_server/listing_exec_app/lib/default_code/ch_13/Listing_13_1Temp.py", shell=True)
	
	matBLACK = open('Code_Listings/Data/plotBLACK1m.txt', 'r')
	pyBLACK = open('Code_Listings/Data/plotBLACK1p.txt', 'r')

	lines1 = matBLACK.read().splitlines()
	lines2 = pyBLACK.read().splitlines()

	returnVal = True
	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)
	matBLACK.close()
	pyBLACK.close()

	os.remove('../web_server/listing_exec_app/lib/default_code/ch_13/Listing_13_1Temp.py')
	print("Complete")
	return returnVal

Listing_1()