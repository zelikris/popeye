import numpy as np
import copy

def addToStruct(strct, fld, text, row, col, nums):
    isNum = isInNums(row, col)
    if isNum:
        value = nums[row-2][col-2]
    else:
        value = text[row][col]
    if fld in strct:
        item = strct[fld]
        item.append(value)
    else:
#        if fld == 'Final':
#            print(fld + ': ' + str(value) 
#                + ' [ ' + str(row) + ', ' + str(col) + ' ]')
        if isNum:
            strct[fld] = [value]
        else:
            strct[fld] = value
    
def isInNums(row, col):
    return (row > 1) and (col > 1)
    
def addField(flds, fld):
    found = False
    for i in range(len(flds)):
        if flds[i] == fld:
            found = True
            break
    if not found:
        flds.append(fld)
  
def isNumCh(ch):
    res = ch in '0123456789-+.'
    return res
      
def _remNos(str):
    i = 0;
    while i < len(str) and not isNumCh(str[i]):
        i = i + 1
    return str[:i]
    
def _parse_a_line(ln):
    at = 0
    nq = 0
    frm = 0
    if len(ln) > 0 and ln[0] == ',':
        fxd_ln = ' '
    else:
        fxd_ln = ''
    while at < len(ln):
        if ln[at] == '"':
            nq = nq + 1
        elif ln[at] == ',' and nq%2 == 1:
            # change comma within quotes to 255
            # copy line up to here and insert 255
            fxd_ln = fxd_ln + ln[frm:at] + chr(255)
            frm = at+1 
        elif at > 0 and (ln[at] == ',' or ln[at] == '\n') and ln[at-1] == ',':
            # sequential commas insert space
            fxd_ln = fxd_ln + ln[frm:at] + ' '
            frm = at        
        at = at + 1
    # then copy the rest of the line
    fxd_ln = fxd_ln + ln[frm:]
#    print(fxd_ln,end="",flush=True)
    # now tokenize it
    tkns = list()
    while len(fxd_ln) > 0:
        tkn, fxd_ln = strtok(fxd_ln, ',\n')
        # repolace the 255's with comma
        if len(tkn) > 0:
            fxd_tkn = ''
            at = 0
            frm = 0
            while at < len(tkn):
                if tkn[at] == chr(255):
                    fxd_tkn = fxd_tkn + tkn[frm:at] + ','
                    frm = at + 1
                at = at + 1
            fxd_tkn = fxd_tkn + tkn[frm:]
            tkns.append(fxd_tkn)  
    return tkns
    
def csvread(name):
    # do Matlab style xlsread on a csv file
    # nums will be a np.array
    # txt and raw will be tuples
    fh = open(name, 'r')
    lines = fh.readlines()
    # get dimensions of the data
    rows = len(lines)
    tkns = _parse_a_line(lines[0])
    cols = len(tkns)
    # now, construct raw data file
    raw = [[[] for i in range(cols)] for i in range(rows)]
    row = 0
    while row < rows:
        for col in range(cols):
            raw[row][col] = tkns[col]
        row = row + 1
        if row < rows:
            tkns = _parse_a_line(lines[row])
    # find the nums array
    # 1. left to right
    col = 0
    found = False;
    while not found and col < cols:
        for row in range(rows):
            wd = raw[row][col]
            if isNumCh(wd[0]):
                found = True
                break
        if not found: col = col + 1
    left = col
    # 2. right to left
    col = cols-1
    found = False;
    while not found and col >= 0:
        for row in range(rows):
            wd = raw[row][col]
            if isNumCh(wd[0]):
                found = True
                break
        if not found: col = col - 1
    right = col
    # 3. top to bottom
    row = 0
    found = False;
    while not found and row < rows:
        for col in range(cols):
            wd = raw[row][col]
            if isNumCh(wd[0]):
                found = True
                break
        if not found: row = row + 1
    top = row
    # 4. bottom to top
    row = rows - 1
    found = False;
    while not found and row >= 0:
        for col in range(cols):
            wd = raw[row][col]
            if isNumCh(wd[0]):
                found = True
                break
        if not found: row = row - 1
    bottom = row
    numRows = bottom+1-top
    numCols = right+1-left
    nums = np.zeros((numRows, numCols))
    txt = copy.deepcopy(raw)
    for numRow in range(numRows):
        for numCol in range(numCols):
            word = raw[numRow+left][numCol+top]
#            if numCol == 8:
#                print('ouch!')
            if isNumCh(word[0]):
                nums[numRow][numCol] = float(word)
                txt[numRow+left][numCol+top] = ''           
            else:
                nums[numRow][numCol] = np.NaN
    return (nums, txt, raw)

def strtok(text, delim):
    at = 0
    n = len(text)
    # skip leading delimiters
    while at < n and text[at] in delim:
        at = at + 1
    # find token
    start = at
    while at < n and text[at] not in delim:
        at = at + 1 
    token = text[start:at]
    rest = text[at:]
    return (token, rest)        


def Listing_01():
# Listing 08.01 Script to list a text file
    file = open("mercy.txt", "r")
    keepGoing = True
    while keepGoing:
        ln = file.readline()
        keepGoing = len(ln) > 0
        if keepGoing:
            print(ln,end="",flush=True)
    file.close()

def Listing_02():
# Listing 08.02 Listing a file using tokens
    file = open("mercy.txt", "r")
    keepGoing = True
    while keepGoing:
        ln = file.readline()
        keepGoing = len(ln) > 0
        if keepGoing:
            print(ln,end="",flush=True)
            keepGoing = len(ln) > 0
            tks = list()
            while keepGoing and (len(ln) > 0):
                tk, ln = strtok(ln, ' \n')
                if len(tk) > 0:
                    tks.append(tk)
            print( str(tks) )
    file.close()
    
def Listing_03():
# Listing 08.03 Listing a file using tokens
    infile = open("mercy.txt", "r")
    outfile = open("nice_mercy.txt", "w")
    keepGoing = True
    while keepGoing:
        ln = infile.readline()
        keepGoing = len(ln) > 0
        if keepGoing:
            keepGoing = len(ln) > 0
            while keepGoing and (len(ln) > 0):
                tk, ln = strtok(ln, ' \n')
                if len(tk) > 0:
                    outfile.write(tk + ' ')
            outfile.write('\n')
    infile.close()
    outfile.close()
    
def Listing_04():
# Listing 08.04 Listing a CSV file
    nums, text, raw = csvread('gradeSheet.csv')
    print('nums = ' + str(nums))
    print('text = ' + str(text))
    print('raw = ' + str(raw))
    # now, make a structure array of the spread sheet
    rows = len(raw)
    cols = len(raw[0])
    print("size of raw is [" + str(rows) + ', ' + str(cols) + ']')
    # make a list of field names 
    flds = list()
    prefix = ' ';
    for col in range(cols):
        if not text[0][col] == ' ':
            prefix = text[0][col]
        if prefix == ' ':
            fld = _remNos(text[1][col])
        else:
            fld = prefix + '_' + _remNos(text[1][col]) 
        addField(flds, fld)
    print('Field names:\n' + str(flds))
    strctArr = list();
    for row in np.arange(2,rows):
        prefix = ' ';
        strct = {}
        for col in range(cols):
            if not text[0][col] == ' ':
                prefix = text[0][col]
            if prefix == ' ':
                fld = _remNos(text[1][col])
            else:
                fld = prefix + '_' + _remNos(text[1][col]) 
            addToStruct(strct, fld, text, row, col, nums)
        strctArr.append(copy.deepcopy(strct))
    print('Everthing:\n' + str(strctArr))
            
#print("\nListing_01\n")
#A = Listing_01();
#print("\nListing_02\n")
#A = Listing_02();
#print("\nListing_03\n")
#A = Listing_03();
print("\nListing_04\n")
A = Listing_04();
