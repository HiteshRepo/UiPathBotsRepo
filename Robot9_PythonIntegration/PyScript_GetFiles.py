import os
 
def count(dir='.', counter=0):
    "returns number of files in dir and subdirs"
    for pack in os.walk(dir):
        for f in pack[2]:
            counter += 1
    return "No of files in '" + dir + "' : " + str(counter) + " files"
 
 
#print(count("."))