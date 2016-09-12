def Listing_04():
#  Listing 04.04 Example of a switch statement
    month = int(input("Give me a month number please.\n-> "))
    for case in switch(month):
       if case(9, 4, 6, 11):
       # Sept, Apr, June, Nov
           days = 30
           break
       if case(2): # Feb
            year = int(input("Give me a year number please.\n-> "))            
            leapYear = 0
            if year % 4 == 0:
                leapYear = 1
            if leapYear:
                days = 29;
            else:
                days = 28;
            break
       if case(1, 3, 5, 7, 8, 10, 12):
            # other months
            days = 31;
            break
       if case():
            print('bad month index')
            break
    print('Month ' + str(month) + " has " + str(days) + ' days')