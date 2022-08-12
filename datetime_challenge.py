import datetime
from datetime import datetime
from pytz import timezone
import pytz

def isBranchOpen(branchTime):
    if branchTime >= 9 and branchTime < 18:
        print("The branch is open.")
    else:
        print("The branch is now closed and will reopen at 9 AM")


#first var with local time
localTime = datetime.now()
localTimePDX = int(localTime.strftime('%H'))
print(localTime.strftime('%I:%M%p'))

isBranchOpen(localTimePDX)
    
#2nd var London time
localTimeLon = localTime.astimezone(timezone('Europe/London'))
LonHour = int(localTimeLon.strftime('%H'))
print(localTimeLon.strftime('%I:%M%p'))


isBranchOpen(LonHour)        



#third var NY time
localTimeNY = localTime.astimezone(timezone('US/Eastern'))
NYHour = int(localTimeNY.strftime('%H'))
print(localTimeNY.strftime('%I:%M%p'))


isBranchOpen(NYHour)
