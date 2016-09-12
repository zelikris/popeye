import sys
import os
import shutil
import subprocess

def Listing_10():
	listingsrc = '../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_10.py'
	shutil.copy(listingsrc, '../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_10Temp.py')
	f1 = open('../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_10Temp.py', 'a')
	f2 = open('Code_Listings/Appends/ap10.txt', 'r')
	for line in f2:
		f1.write(line)
	f1.close()
	f2.close()

	subprocess.call("python ../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_10Temp.py", shell=True)
	
	matxx = open('Code_Listings/Data/plotxx8m.txt', 'r')
	pyxx = open('Code_Listings/Data/plotxx8p.txt', 'r')

	lines1 = matxx.read().splitlines()
	lines2 = pyxx.read().splitlines()

	returnVal = True
	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)
	matxx.close()
	pyxx.close()

	matyy = open('Code_Listings/Data/plotyy8m.txt', 'r')
	pyyy = open('Code_Listings/Data/plotyy8p.txt', 'r')

	lines1 = matyy.read().splitlines()
	lines2 = pyyy.read().splitlines()

	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)
	matyy.close()
	pyyy.close()

	matzz = open('Code_Listings/Data/plotzz8m.txt', 'r')
	pyzz = open('Code_Listings/Data/plotzz8p.txt', 'r')

	lines1 = matzz.read().splitlines()
	lines2 = pyzz.read().splitlines()

	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)
	matzz.close()
	pyzz.close()

	os.remove('../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_10Temp.py')
	print("Complete")
	return returnVal

def Listing_9():
	listingsrc = '../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_9.py'
	shutil.copy(listingsrc, '../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_9Temp.py')
	f1 = open('../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_9Temp.py', 'a')
	f2 = open('Code_Listings/Appends/ap9.txt', 'r')
	for line in f2:
		f1.write(line)
	f1.close()
	f2.close()

	subprocess.call("python ../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_9Temp.py", shell=True)
	
	matxx = open('Code_Listings/Data/plotxx9m.txt', 'r')
	pyxx = open('Code_Listings/Data/plotxx9p.txt', 'r')

	lines1 = matxx.read().splitlines()
	lines2 = pyxx.read().splitlines()

	returnVal = True
	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)

	matxx.close()
	pyxx.close()

	matyy = open('Code_Listings/Data/plotyy9m.txt', 'r')
	pyyy = open('Code_Listings/Data/plotyy9p.txt', 'r')

	lines1 = matyy.read().splitlines()
	lines2 = pyyy.read().splitlines()

	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)

	matyy.close()
	pyyy.close()

	matzz = open('Code_Listings/Data/plotzz9m.txt', 'r')
	pyzz = open('Code_Listings/Data/plotzz9p.txt', 'r')

	lines1 = matzz.read().splitlines()
	lines2 = pyzz.read().splitlines()

	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)

	matzz.close()
	pyzz.close()

	os.remove('../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_9Temp.py')
	print("Complete")
	return returnVal

def Listing_13():
	listingsrc = '../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_13.py'
	shutil.copy(listingsrc, '../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_13Temp.py')
	f1 = open('../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_13Temp.py', 'a')
	f2 = open('Code_Listings/Appends/ap13.txt', 'r')
	for line in f2:
		f1.write(line)
	f1.close()
	f2.close()

	subprocess.call("python ../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_13Temp.py", shell=True)
	
	matxx = open('Code_Listings/Data/plotxx13m.txt', 'r')
	pyxx = open('Code_Listings/Data/plotxx13p.txt', 'r')

	lines1 = matxx.read().splitlines()
	lines2 = pyxx.read().splitlines()

	returnVal = True
	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:	
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)

	matxx.close()
	pyxx.close()

	matyy = open('Code_Listings/Data/plotyy13m.txt', 'r')
	pyyy = open('Code_Listings/Data/plotyy13p.txt', 'r')

	lines1 = matyy.read().splitlines()
	lines2 = pyyy.read().splitlines()

	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:	
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)

	matyy.close()
	pyyy.close()

	matzz = open('Code_Listings/Data/plotzz13m.txt', 'r')
	pyzz = open('Code_Listings/Data/plotzz13p.txt', 'r')

	lines1 = matzz.read().splitlines()
	lines2 = pyzz.read().splitlines()

	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:	
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)

	matzz.close()
	pyzz.close()

	os.remove('../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_13Temp.py')
	print("Complete")
	return returnVal

def Listing_12():
	listingsrc = '../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_12.py'
	shutil.copy(listingsrc, '../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_12Temp.py')
	f1 = open('../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_12Temp.py', 'a')
	f2 = open('Code_Listings/Appends/ap12.txt', 'r')
	for line in f2:
		f1.write(line)
	f1.close()
	f2.close()

	subprocess.call("python ../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_12Temp.py", shell=True)
	
	matxx = open('Code_Listings/Data/plotxx12m.txt', 'r')
	pyxx = open('Code_Listings/Data/plotxx12p.txt', 'r')

	lines1 = matxx.read().splitlines()
	lines2 = pyxx.read().splitlines()

	returnVal = True
	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:	
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)

	matxx.close()
	pyxx.close()

	matyy = open('Code_Listings/Data/plotyy12m.txt', 'r')
	pyyy = open('Code_Listings/Data/plotyy12p.txt', 'r')

	lines1 = matyy.read().splitlines()
	lines2 = pyyy.read().splitlines()

	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:	
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)

	matyy.close()
	pyyy.close()

	matzz = open('Code_Listings/Data/plotzz12m.txt', 'r')
	pyzz = open('Code_Listings/Data/plotzz12p.txt', 'r')

	lines1 = matzz.read().splitlines()
	lines2 = pyzz.read().splitlines()

	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:	
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)

	matzz.close()
	pyzz.close()

	os.remove('../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_12Temp.py')
	print("Complete")
	return returnVal

def Listing_5():
	listingsrc = '../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_5.py'
	shutil.copy(listingsrc, '../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_5Temp.py')
	f1 = open('../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_5Temp.py', 'a')
	f2 = open('Code_Listings/Appends/ap5.txt', 'r')
	for line in f2:
		f1.write(line)
	f1.close()
	f2.close()

	subprocess.call("python ../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_5Temp.py", shell=True)
	
	matxx = open('Code_Listings/Data/plotxx5m.txt', 'r')
	pyxx = open('Code_Listings/Data/plotxx5p.txt', 'r')

	lines1 = matxx.read().splitlines()
	lines2 = pyxx.read().splitlines()

	returnVal = True
	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:	
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)

	matxx.close()
	pyxx.close()

	matyy = open('Code_Listings/Data/plotyy5m.txt', 'r')
	pyyy = open('Code_Listings/Data/plotyy5p.txt', 'r')

	lines1 = matyy.read().splitlines()
	lines2 = pyyy.read().splitlines()

	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:	
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)

	matyy.close()
	pyyy.close()

	matzz = open('Code_Listings/Data/plotzz5m.txt', 'r')
	pyzz = open('Code_Listings/Data/plotzz5p.txt', 'r')

	lines1 = matzz.read().splitlines()
	lines2 = pyzz.read().splitlines()

	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:	
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)

	matzz.close()
	pyzz.close()


	os.remove('../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_5Temp.py')
	print("Complete")
	return returnVal

def Listing_16():
	listingsrc = '../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_16.py'
	shutil.copy(listingsrc, '../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_16Temp.py')
	f1 = open('../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_16Temp.py', 'a')
	f2 = open('Code_Listings/Appends/ap16.txt', 'r')
	for line in f2:
		f1.write(line)
	f1.close()
	f2.close()

	subprocess.call("python ../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_16Temp.py", shell=True)
	
	matxx = open('Code_Listings/Data/plotxx5m.txt', 'r')
	pyxx = open('Code_Listings/Data/plotxx5p.txt', 'r')

	lines1 = matxx.read().splitlines()
	lines2 = pyxx.read().splitlines()

	returnVal = True
	for x in range(0, len(lines1)):
		if (lines1[x].strip() != lines2[x].strip()):
			print "Testing Failed!"
			returnVal = False
		else:	
			pri = lines1[x].strip() + " " + lines2[x].strip() + " Correct!"
			print (pri)

	matxx.close()
	pyxx.close()
	os.remove('../web_server/listing_exec_app/lib/default_code/ch_11/Listing_11_16Temp.py')
	print("Complete")
	return returnVal

Listing_5()
Listing_9()
Listing_10()
Listing_12()
Listing_13()
Listing_16()