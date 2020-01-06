#code challenge / 1.6.2020, S Krishna
#create a seating program that accepts groups for 1=>N<=1000 seats.
#groups need not sit together. seat allocated as available.
#if one group member leaves everyone leaves.
#if seat availability < group size then dont accept.

#global var for group ID to keep track of groups
gid = 1

#method to check how many seats are available
def availableSeats(seatlisting):
    emptyCount = 0
    for item in seatlisting:
        if(not bool(item)):  #if seat is not taken
            emptyCount=emptyCount+1 #increment counter

    return emptyCount

#method to assign seats to eligible groups in a dictionary array
def assignPersonToSeat(seatlisting,peopleCount):
        count=0;
        for position,items in enumerate(seatlisting):
            if(not bool(items)): #if empty seat available
                count=count+1
                if(count<=peopleCount): #if group value still valid
                    seatlisting[position] = dict({gid:"X"}) #assign person and group id

#method to assign seats to eligible groups in a dictionary array
def removePersonGroup(seatlisting,position):
    #temp variable to hold keys being looked for.
    keysvar= seatlisting[position].keys()
    if(bool(seatlisting[position])): #if seat has someone in it
        for i in range(len(seatlisting)): #loop through seatlisting
            if(seatlisting[i].keys()==keysvar): #if keys match
                seatlisting[i]=dict({}) #make it available


#main program starts here
#open data file and read from it
iFile = open("input.txt","r")
linesInFile = iFile.readlines()
maxSeats = linesInFile[0]  #read first line and create dict array based on max size
#create an array of dictionaries. each value-key pair will hold group info.
seatlisting = [dict() for x in range(int(maxSeats))]

#loop through file contents
for line in linesInFile:
    #for each line check if people are arriving or leaving
    if(line.split()[0]=="A"):
        peopleCount = line.split()[1] #get the first element on line (either A or l)
        #check if enough seats available
        if(availableSeats(seatlisting)>=int(peopleCount)):
            assignPersonToSeat(seatlisting,int(peopleCount)) #assign seats
            gid=gid+1 #successful assignment of one group
            print(seatlisting) #print latest version of seating

    if(line.split()[0]=="L"):
        posRemove = line.split()[1] #remove person/group at this position
        removePersonGroup(seatlisting,int(posRemove)) #remove group
        print(seatlisting) #print latest version of seating
